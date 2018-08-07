from django.contrib import admin
# from blog.models import Article
from jobs.models import Job,JobCategory
# Register your models here.
# admin.site.register(Article)
class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','slug')
	prepopulated_fields= {'slug':('name',)}
class JobAdmin(admin.ModelAdmin):
	list_display=('title','location','date_posted','company_name')
	prepopulated_fields= {'tags':('title',)}
admin.site.register(Job,JobAdmin)
admin.site.register(JobCategory,CategoryAdmin)

