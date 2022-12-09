from rest_framework import serializers

from advertisement.models import Media, Reward


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["uuid", "title", "description", "company", "campaigns", "zone"]


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["uuid", "title", "description", "type", "share_count", "view_count"]
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['pk', 'created_on', 'is_valid', 'offered_by', 'count', 'token_value']