from management.models import Campaign, Company, Zone
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "pk",
            "name",
            "web_url",
            "is_active",
            "country",
            "city",
            "street",
            "house_no",
        ]


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ["pk", "name", "description", "start_date", "end_date", "company"]
        depth = 1
