import os

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from firebase_auth.exceptions import NoAuthToken, InvalidAuthToken, FirebaseError

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
        "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL"),
    }
)

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

            print (decoded_token.get("user_id"))
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