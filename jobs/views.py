from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import JobSerializer
from jobs.models import Job
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jobs.forms import CreateJob

def jobsIndex(request):
	queryset_list=Job.objects.all().order_by('-date_posted')
	paginator = Paginator(queryset_list,20)
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
