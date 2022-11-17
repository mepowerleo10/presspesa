from django.contrib import admin
from .models import Campaign, Company, Token, Zone

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    """Admin View for Campaign"""

    list_display = ('name', 'company', 'start_date', 'end_date')
    list_filter = ('name', 'company')
    ordering = ('-end_date',)


class CampaignInline(admin.TabularInline):
    model = Campaign


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'date_joined', 'city')
    ordering = ('-date_joined', 'name',)
    serach_fields = ('name', 'city', 'street')
    inlines = [CampaignInline]




@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    """Admin View for Token"""

    list_display = ('offered_by', 'is_valid', 'count', 'token_value',)
    ordering = ('-created_on',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    """Admin View for Zone"""

    list_display = ('name', 'campaign',)
