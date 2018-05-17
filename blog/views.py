from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post 
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from blog.forms import CreatePost
# Create your views here.
@login_required(login_url='/login')
def index(request):
	queryset_list=Post.objects.all().order_by('-date_published')
	paginator = Paginator(queryset_list,3)
	page = request.GET.get('page')
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(Q(title__icontains=query))

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset =paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(Paginator.num_pages)
	context={
	"queryset":queryset,
	"page":page}
	return render(request,"blog/post.html",context)

@login_required(login_url='/login')
def create_post(request):
	if request.method=='POST':
		form = CreatePost(request.POST,request.FILES)
		if form.is_valid():
			#save to the database
			instance= form.save(commit=False)
			instance.posted_by = request.user
			instance.save()
			return redirect('/post')
	else:
		form=CreateJob()
	return render(request,'jobs/create_job.html',{'form':form})
