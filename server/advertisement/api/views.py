from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from advertisement.models import Advertisement, Media
from .serializers import MediaSerializer


class MediaView(GenericAPIView):
    def get(self, request):
        adverts = Advertisement.objects.all().first()
        media: Media = adverts.media.all()
        serializer = MediaSerializer(media)
        return Response(serializer.data)

class MediaListView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer