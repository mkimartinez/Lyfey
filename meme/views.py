from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django import forms
from django.contrib import auth
from meme.models import Mem
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . import forms

# def indexMemes(request):
# 	return render(request, 'memes/index.html')
# # def index(request):
#     return render(request, 'library/index.html')
@login_required(login_url='/login')
def index(request):
	model=Mem
	queryset_list=model.objects.all().order_by('date_posted')
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
	return render(request,"meme/index.html",context)

# class MemeCreate(CreateView):
# 	model = is_empty_element()
# 	fields = ['banner','title']

@login_required(login_url='/login')
def meme_create(request):
	
	if request.method=='POST':
		form = forms.CreateMeme(request.POST,request.FILES)
		if form.is_valid():
			#safe meme to db
			instance= form.save(commit=False)
			instance.publisher = request.user
			instance.save()
			return redirect('meme:indexMemes')
			# return (HttpResponse("sucess"))
	else:
		form = forms.CreateMeme()

	return render(request,'meme/meme_create.html',{'form':form})
