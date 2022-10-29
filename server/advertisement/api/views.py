from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from advertisement.models import Advertisement, Media
from .serializers import MediaSerializer


@api_view(["POST"])
def watch_video(request, uuid):
    video = Media.objects.get(uuid=uuid)
    video.view_count += 1
    video.save()

    serializer = MediaSerializer(video)
    return Response(serializer.data)

class MediaView(GenericAPIView):
    def get(self, request):
        adverts = Advertisement.objects.all().first()
        media: Media = adverts.media.all()
        serializer = MediaSerializer(media)
        return Response(serializer.data)

class MediaListView(ListAPIView):
    queryset = Media.objects.filter(is_done_processing=True)
    serializer_class = MediaSerializer