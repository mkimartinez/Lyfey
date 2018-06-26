from django.contrib import admin
from cityEvent.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display=('title','date_posted','county')
	# prepopulated_fields= {'tags':('title',)}
# Register your models here.

admin.site.register(Event,EventAdmin)