from django.contrib import admin
from blog.models import Post,Category,BlogComment

class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','slug')
	prepopulated_fields= {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','date_published','category')
	prepopulated_fields= {'tags':('title',)}


class PostCommentAdmin(admin.ModelAdmin):
	list_display=('post','commented_by','date','comment')
# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(BlogComment,PostCommentAdmin)
 
