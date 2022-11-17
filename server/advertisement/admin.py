from django.contrib import admin
from advertisement.models import Advertisement, Media
# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    '''Admin View for Advertisement'''

    list_display = ('title', 'company')
    search_fields = ('title', 'company', 'zone', 'campaigns')
    ordering = ('-created_on',) 

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    '''Admin View for Media'''
    list_display = ('title', 'type', 'share_count', 'view_count',)
    search_fields = ('title', 'campaigns', 'type')