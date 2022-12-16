from django.contrib import admin
from django.http import HttpRequest
from .models import Campaign, Company, Credit, CreditDebt, CreditOffering, Zone


class ZoneInline(admin.TabularInline):
    model = Zone


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    inlines = [ZoneInline]
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


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    pass

    list_display = ('offered_by', 'is_valid', 'count', 'token_value',)
    ordering = ('-created_on',)

@admin.register(CreditOffering)
class CreditOfferingAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request: HttpRequest, obj):
        if obj:
            return ["amount", "to", "on"]
        else:
            return []

@admin.register(CreditDebt)
class CreditDebtAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request: HttpRequest, obj):
        if obj:
            return ["amount", "to", "on"]
        else:
            return []

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    """Admin View for Zone"""

    list_display = ('name', 'campaign',)
