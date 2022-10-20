import os

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from firebase_auth.exceptions import NoAuthToken, InvalidAuthToken, FirebaseError

from config.settings import env

cred = credentials.Certificate(env("FIREBASE_SERVICE_ACCOUNT_KEY_PATH"))

default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token.get("user_id")

            print(decoded_token.get("user_id"))
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        try:
            uid = decoded_token.get("uid")
            phone_number = decoded_token.get("phone_number")
        except Exception:
            raise FirebaseError()
        User = get_user_model()
        user, created = User.objects.get_or_create(username=uid, phone_no=phone_number)

        return (user, None)
