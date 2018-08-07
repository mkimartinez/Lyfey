from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib import auth
from cityEvent.models import Event
from django.template import loader
from .forms import PostEvent
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

 
def index(request):
	queryset_list=Event.objects.all().order_by('-date_posted')
	query = request.GET.get("query")
	if query:
		queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(location__icontains=query))

	page = request.GET.get('page')
	paginator = Paginator(queryset_list, 6)

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset =paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(Paginator.num_pages)
	context={
	"queryset":queryset,
	"page":page}
	return render(request,'cityevent/event_index.html',context)


@login_required(login_url='/login')
def post_event(request):
	if request.method=='POST':
		form = PostEvent(request.POST,request.FILES)
		if form.is_valid():
			#save to the database
			instance= form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('cityEvent:event_index')
	else:
		form=PostEvent()
	return render(request,'cityEvent/post_event.html',{'form':form})



def event_detail(request,pk):
	event_q=Event.objects.all().order_by('-event_date')[:4]
	try:
		event_id=Event.objects.get(pk=pk)
	except Event.DoesNotExist:
		raise Http404("post does not exist")
	return render(request, 'cityEvent/event_detail.html',context={'event':event_id,'event_q':event_q }
)