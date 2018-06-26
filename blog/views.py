from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category,BlogComment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
from jobs.forms import CreateJob
from.serializer import PostSerializer,CategorySerializer
from rest_framework import viewsets
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from blog.forms import CreatePost,CreateComment


# Create your views here.

def index(request):
    queryset_list=Post.objects.all().order_by('-date_published')
    query = request.GET.get("query")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(tags__icontains=query))
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
        "categories":Category.objects.all(),
        "page":page}
    return render(request,"blog/post.html",context)


def blog_detail(request):
    pass

class PostDetailView(generic.DetailView):
    model = Post

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

@login_required(login_url='/login')
def create_comment(request):
    if request.method=='POST':
        form = CreateComment(request.POST,request.FILES)
        if form.is_valid():
            #save to the database
            instance= form.save(commit=False)
            instance.commented_by = request.user
            instance.save()
            return redirect('blog:blog_detail')
    else:
        form=CreateComment()
    return render(request,'blog/post.html',{'form':form})


def categories(request):
    context ={
        'category_list':Category.objects.all()
    }
    return render(request,'blog/categories.html',context)


class PostList(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = PostSerializer(categories,many=True)
        return Response(serializer.data)


class CategoriesList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commented_by=request.user
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CreateComment()
    return render(request, 'blog/post_comment.html', {'form': form})

def post_detail(request,pk):
    post_q=Post.objects.all().order_by('-date_published')[:5]
    try:
        post_id=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("post does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'blog/blog_detail.html',
        context={'post':post_id,'post_q':post_q }
    )