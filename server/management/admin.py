from django.contrib import admin
from .models import Address, Advertisement, Campaign, Company, Media, Token, Zone

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    '''Admin View for Address'''

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

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    '''Admin View for Campaign'''

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

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    '''Admin View for Company'''

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

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    '''Admin View for Token'''

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

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    '''Admin View for Zone'''

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