from django.urls import path 
from .views import MediaListView, MediaView

urlpatterns = [
    path("ads/next/", MediaView.as_view(), name="next_media"),
    path("ads/", MediaListView.as_view(), name="api_media_list"),
]
