from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import Campaign, Company, Zone
from advertisement.models import Advertisement, Media
from .serializers import MediaSerializer


class MediaView(GenericAPIView):
    def get(self, request):
        adverts = Advertisement.objects.all().latest("created_on")
        media: Media = adverts.media.first()
        serializer = MediaSerializer(media)
        return Response(serializer.data)
