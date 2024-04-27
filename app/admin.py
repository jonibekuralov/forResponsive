from django.contrib import admin
from .models import Resource, Contact, HomeModel, footerData, Location, Libary


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


admin.site.register(HomeModel)
admin.site.register(Contact)
admin.site.register(footerData)
admin.site.register(Location)
admin.site.register(Libary)
