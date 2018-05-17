from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from quiz.models import Question
from django.template import loader
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/login')
def index(request):
	queryset_list=Question.objects.all()
	paginator = Paginator(queryset_list,3)
	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset =paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(Paginator.num_pages)
	context={
	"queryset":queryset,
	"page":page}
	return render(request,'quiz/index.html',context)