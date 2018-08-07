from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import JobSerializer
from jobs.models import Job,JobCategory
from django.contrib import messages
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jobs.forms import CreateJob


def jobsIndex(request,category_slug=None):
    category = None
    categories = JobCategory.objects.all()
    queryset_list = Job.objects.all().order_by('-date_posted')
    if category_slug:
        category = get_object_or_404(JobCategory,slug=category_slug)
        queryset_list = Job.objects.filter(category=category)

    page = request.GET.get('page', 1)
    paginator = Paginator(queryset_list,15)
    try:
        number = paginator.page(page)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    context={
        "number":number,
        'category': category,
        "categories": categories,
        "page":page}
    return render(request,"jobs/jobsIndex.html",context)


@login_required(login_url='/login')
def create_job(request):
	if request.method=='POST':
		form = CreateJob(request.POST,request.FILES)
		if form.is_valid():
			#save to the database
			instance= form.save(commit=False)
			instance.posted_by = request.user
			instance.save()
			messages.success(request, 'Job was posted successfully!' ,extra_tags='alert')  
			return redirect('jobs:jobsIndex')
	else:
		form=CreateJob()
	return render(request,'jobs/create_job.html',{'form':form})

class JobList(APIView):
	def get(self,request):
		jobs = Job.objects.all()
		serializer = JobSerializer(jobs,many=True)
		return Response(serializer.data)

	def post(self):
		pass


def job_detail(request,pk):
    jobList=Job.objects.all().order_by('-date_posted')[:5]
    try:
        job_id=Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        raise Http404("post does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'jobs/job_detail.html',
        context={'job':job_id,'jobList':jobList }
    )
