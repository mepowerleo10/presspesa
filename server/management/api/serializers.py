from rest_framework import serializers

from advertisement.models import Media

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "uuid",
            "title",
            "description",
            "company",
            "campaigns",
            "zone"
        ]

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            "uuid",
            "media_title",
            "media_description",
            "media_type"
        ]