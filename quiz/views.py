from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404,Http404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from quiz.models import Question,Answer
from django.template import loader
from django.contrib import messages
from django.db.models import Q
from quiz.forms import AnswerQuestion,AskQuestion
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	queryset_list=Question.objects.all().order_by('-date_posted')
	answer=Answer.objects.all()
	query = request.GET.get("query")
	if query:
		queryset_list=queryset_list.filter(
			Q(content__icontains = query))
	page = request.GET.get('page')
	paginator = Paginator(queryset_list, 5)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset =paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(Paginator.num_pages)
	context={
	"queryset":queryset,
	"answer":answer,
	"page":page}
	return render(request,'quiz/quiz_index.html',context)

def question_details(request,pk):
	quiz=Question.objects.all().order_by('-date_posted')[:5]
	try:
		quiz_id =Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(
		request,
		'quiz/question_details.html',
		context={
		'question':quiz_id,
		'quiz':quiz
		}
		)
@login_required(login_url='/login')
def answer_question(request,pk):
	quiz = get_object_or_404(Question, pk=pk)
	if request.method=='POST':
		form = AnswerQuestion(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.question =quiz
			instance.answered_by=request.user
			instance.save()
			return redirect('quiz:question_details',pk=quiz.pk)
	else:
		form=AnswerQuestion()
	return render(request,'quiz/answer_question.html',{'form':form})

@login_required(login_url='/login')
def ask_question(request):
	if request.method=='POST':
		form = AskQuestion(request.POST,request.FILES)
		if form.is_valid():
			#safe meme to db
			instance= form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request, 'Your question was posted successfully!' ,extra_tags='alert')  
			return redirect('quiz:quiz_index')
		
		else:
			messages.warning(request, 'Please correct the error below.') 
			# return (HttpResponse("sucess"))
	else:
		form =AskQuestion()
		messages.success(request, 'Form can not be empty!' ,extra_tags='alert')  

	return render(request,'quiz/ask_question.html',{'form':form})
