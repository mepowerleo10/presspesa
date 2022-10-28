from django.contrib import admin
from .models import Campaign, Company, Token, Zone

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


class CampaignInline(admin.TabularInline):
    model = Campaign


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CampaignInline]




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
