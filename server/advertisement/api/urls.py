from django.urls import path
from .views import MediaListView, MediaView, watch_video

urlpatterns = [
    path("", MediaListView.as_view(), name="api_media_list"),
    path("next/", MediaView.as_view(), name="api_next_media"),
    path("watch/<uuid:uuid>", watch_video, name="api_watch_video"),
]
