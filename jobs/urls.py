from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings
import jobs.views as views
from django.views.generic import ListView,DetailView
from jobs.models import Job

# urlpatterns = [
#                   url(r'^$', views.indexJobs, name='indexJobs'),
app_name ='jobs'
#                   ]
urlpatterns = [
				  url(r'^$', views.jobsIndex, name='jobsIndex'),
				  url(r'^create/$',views.create_job,name='jobsCreate'),
                  # url(r'^$', ListView.as_view(queryset= Job.objects.all().order_by("-date_posted")[:25],
                  # 	template_name = "jobs/jobsIndex.html")),
                  url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Job,template_name="jobs/job_detail.html"))
                  ]