from django.urls import path
from .views import MediaListView, MediaView, watch_video, RewardDetails, RewardList

urlpatterns = [
    path("", MediaListView.as_view(), name="api_media_list"),
    path("next/", MediaView.as_view(), name="api_next_media"),
    path("watch/<uuid:uuid>", watch_video, name="api_watch_video"),
    # Token Endpoints
    path(
        "rewards/", RewardList.as_view(), name="tokens"
    ),  # Endpoint for listing all tokens
    path(
        "rewards/<int:pk>/", RewardDetails.as_view(), name="token_details"
    ),  # Endpoint for retrieving , update or delete a token instance
    # Token Endpoints
]
