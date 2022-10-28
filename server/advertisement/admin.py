from django.contrib import admin
from advertisement.models import Advertisement, Media
# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    '''Admin View for Advertisement'''

    """ list_display = ('',)
    list_filter = ('',)
    inlines = [
        Inline,
    ]
    raw_id_fields = ('',)
    readonly_fields = ('',)
    search_fields = ('',)
    date_hierarchy = ''
    ordering = ('',) """

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    '''Admin View for Media'''

    """ list_display = ('',)
    list_filter = ('',)
    inlines = [
        Inline,
    ]
    raw_id_fields = ('',)
    readonly_fields = ('',)
    search_fields = ('',)
    date_hierarchy = ''
    ordering = ('',) """