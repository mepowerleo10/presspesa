from django.urls import path 
from .views import MediaView

urlpatterns = [
    path("ads/next/", MediaView.as_view(), name="next_media"),
]
