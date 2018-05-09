from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings
import contacts.views as views
from django.views.generic import ListView,DetailView
from contacts.models import ContactForm

# urlpatterns = [
#                   url(r'^$', views.indexJobs, name='indexJobs'),
app_name ='contacts'
#                   ]
urlpatterns = [
				  url(r'^$', views.sendMessage, name='sendMessage'),
				  # url(r'^create/$',views.create_job,name='jobsCreate'),
      #             # url(r'^$', ListView.as_view(queryset= Job.objects.all().order_by("-date_posted")[:25],
      #             # 	template_name = "jobs/jobsIndex.html")),
      #             url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Job,template_name="jobs/job_detail.html"))
                  ]