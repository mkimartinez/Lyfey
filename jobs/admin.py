from django.contrib import admin
# from blog.models import Article
from jobs.models import Job
# Register your models here.
# admin.site.register(Article)

class JobAdmin(admin.ModelAdmin):
	list_display=('title','location','date_posted','company_name')
	prepopulated_fields= {'tags':('title',)}
admin.site.register(Job,JobAdmin)
