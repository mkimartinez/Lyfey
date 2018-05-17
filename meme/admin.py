from django.contrib import admin
from .import models
from meme.models import Comment 

# Register your models here.
admin.site.register(models.Mem)

class CommentAdmin(admin.ModelAdmin):
	list_display =('user','email','approved')
admin.site.register(Comment,CommentAdmin)