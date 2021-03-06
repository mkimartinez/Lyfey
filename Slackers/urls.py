from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('library.urls')),
    # url(r'^library/', include('library.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^meme/', include('meme.urls')),
    url(r'^cityEvent/', include('cityEvent.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'ckeditor/',include('ckeditor_uploader.urls')),
]
