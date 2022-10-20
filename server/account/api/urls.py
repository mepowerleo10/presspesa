# from django.conf.urls import url
import imp
from django.urls import path 
from account.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name="firebase_register"),
]
