from django.contrib import admin
from .models import Address, Advertisement, Campaign, Company, Media, Token, Zone


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin View for Address"""

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


class CampaignInline(admin.StackedInline):
    model = Campaign


class CompanyInline(admin.TabularInline):
    model = Company


class ZoneInline(admin.TabularInline):
    model = Zone


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Admin View for Advertisement"""

    """ inlines = [
        CompanyInline, CampaignInline, ZoneInline, MediaInline
    ] """


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    """Admin View for Campaign"""

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
    inlines = [CampaignInline]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    """Admin View for Media"""

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


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    """Admin View for Zone"""

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
