from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('library.urls')),
    url(r'^library/', include('library.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^meme/', include('meme.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'ckeditor/',include('ckeditor_uploader.urls')),
]
