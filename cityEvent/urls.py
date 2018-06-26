from django.conf.urls import url,include
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView,DetailView
from cityEvent import views
from cityEvent.models import Event

app_name='cityEvent'

urlpatterns=[
			url(r'^$', views.index, name='event_index'),
			url(r'^create/$',views.post_event,name='eventsCreate'),
			# url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Event,template_name="cityEvent/event_detail.html"))
			url(r'^(?P<pk>\d+)$',views.event_detail,name='event_detail')
			]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#                   url(r'^$', ListView.as_view(queryset= Post.objects.all().order_by("-date_published")[:5],
#                   	template_name = "blog/post.html")),
#                   url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog/blog_detail.html"))
#                   ]