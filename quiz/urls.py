from django.conf.urls import url,include
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView,DetailView
from quiz import views


urlpatterns=[
			url(r'^$', views.index, name='index'),
			# url(r'^create/$',views.create_post,name='postCreate'),
			# url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Event,template_name="cityEvent/event_detail.html"))

			]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#                   url(r'^$', ListView.as_view(queryset= Post.objects.all().order_by("-date_published")[:5],
#                   	template_name = "blog/post.html")),
#                   url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog/blog_detail.html"))
#                   ]