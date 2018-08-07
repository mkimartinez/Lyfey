from django.contrib import admin
from library.models import Subscribe

admin.site.name = 'Lyfey Kenya'
admin.site.site_header = 'Lyfey Kenya'


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email','username')

admin.site.register(Subscribe, SubscribeAdmin)
