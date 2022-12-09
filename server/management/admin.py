from django.contrib import admin
from django.http import HttpRequest
from .models import Campaign, Company, Credit, CreditDebt, CreditOffering, Zone


class ZoneInline(admin.TabularInline):
    model = Zone


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    inlines = [ZoneInline]


class CampaignInline(admin.TabularInline):
    model = Campaign


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CampaignInline]


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    pass


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
