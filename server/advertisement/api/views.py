from advertisement.models import Advertisement, Media, Reward
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MediaSerializer, RewardSerializer


@api_view(["POST"])
def watch_video(request, uuid):
    video = Media.objects.get(uuid=uuid)
    video.view_count += 1
    video.save()

    serializer = MediaSerializer(video)
    return Response(serializer.data)


class MediaView(generics.GenericAPIView):
    def get(self, request):
        adverts = Advertisement.objects.all().first()
        media: Media = adverts.media.all()
        serializer = MediaSerializer(media)
        return Response(serializer.data)


class MediaListView(generics.ListAPIView):
    queryset = Media.objects.filter(is_done_processing=True).filter()
    serializer_class = MediaSerializer


class RewardList(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer


class RewardDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
