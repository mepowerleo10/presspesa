from django.contrib import admin
from advertisement.models import Advertisement, Media, Reward

# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Admin View for Advertisement"""


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    """Admin View for Media"""


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    """Admin View for Token"""

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
