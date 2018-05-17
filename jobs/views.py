from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from jobs.models import Job
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jobs.forms import CreateJob

# Create your views here.

# def indexJobs(request):
# 	return HttpResponse("Hi")
@login_required(login_url='/login')
def jobsIndex(request):
	queryset_list=Job.objects.all().order_by('-date_posted')
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
	return render(request,"jobs/jobsIndex.html",context)


# @login_required(login_url='/login')
# def meme_create(request):
	
# 	if request.method=='POST':
# 		form = forms(request.POST,request.FILES)
# 		if form.is_valid():
# 			#safe meme to db
# 			return redirect('/memes')
# 			# return (HttpResponse("sucess"))
# 	else:
# 		form = forms.CreateMeme()

# 	return render(request,'memes/meme_create.html',{'form':form})

@login_required(login_url='/login')
def create_job(request):
	if request.method=='POST':
		form = CreateJob(request.POST,request.FILES)
		if form.is_valid():
			#save to the database
			instance= form.save(commit=False)
			instance.posted_by = request.user
			instance.save()
			return redirect('jobs:jobsIndex')
	else:
		form=CreateJob()
	return render(request,'jobs/create_job.html',{'form':form})
