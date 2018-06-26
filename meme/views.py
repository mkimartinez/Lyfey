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
from meme.forms import CreateMem,MemeComment

def index(request):
	model=Mem
	queryset_list=model.objects.all().order_by('-date_posted')
	paginator = Paginator(queryset_list,6)
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
		form = CreateMem(request.POST,request.FILES)
		if form.is_valid():
			#safe meme to db
			instance= form.save(commit=False)
			instance.publisher = request.user
			instance.save()
			return redirect('meme:indexMemes')
			# return (HttpResponse("sucess"))
	else:
		form = CreateMem()

	return render(request,'meme/meme_create.html',{'form':form})

def meme_details(request,pk):
	memeList= Mem.objects.all().order_by('-date_posted')[:10]
	try:
		mem_id = Mem.objects.get(pk=pk)
	except Mem.DoesNotExist:
		raise Http4o4("Does not exist")
	return render(request,'meme/meme_details.html',
		context={'mem':mem_id,'memeList':memeList})

def meme_comment(request,pk):
	meme = get_object_or_404(Mem, pk=pk)
	if request.method=='POST':
		form =MemeComment(request.POST,request.FILES)
		if form.is_valid():
            #save to the database
			instance= form.save(commit=False)
			instance.user = request.user
			instance.meme = meme
			instance.save()
			return redirect('meme:meme_details',pk=meme.pk)
	else:
		form=MemeComment()
	return render(request,'meme/meme_comment.html',{'form':form})
# def post_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CreateComment(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.commented_by=request.user
#             comment.post = post
#             comment.save()
#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = CreateComment()
#     return render(request, 'blog/post_comment.html', {'form': form})