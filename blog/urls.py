from django.conf.urls import url,include
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView,DetailView
from django.contrib.sitemaps.views import sitemap
from blog.models import Post,Category
from rest_framework.urlpatterns import format_suffix_patterns
import blog.views as views
from rest_framework import routers
# from .sitemaps import PostSitemap

app_name="blog"

router = routers.DefaultRouter()
router.register('posts',views.PostView)
router.register('categories',views.CategoriesList)
# path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

urlpatterns=[
			url(r'^$', views.index, name='index'),
			# url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
			url('',include(router.urls)),
			url(r'^postList/', views.PostList.as_view()),
			url(r'^(?P<category_slug>[-\w]+)/$', views.index, name='post_by_category'),
				# url(r'^create/$',views.create_post,name='postCreate'),
			url(r'^(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
			# url(r'^(?P<pk>\d+)$',views.PostDetailView.as_view(),name='blog_detail'),
			url(r'^(?P<pk>\d+)$',views.post_detail,name='post_detail'),
			# url(r'^category/(?P<category_slug>[-\w]+)$',views.post_category,name='post_category')
			]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = [
#                   url(r'^$', ListView.as_view(queryset= Post.objects.all().order_by("-date_published")[:5],
#                   	template_name = "blog/post.html")),
#                   url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog/blog_detail.html"))
#                   ]