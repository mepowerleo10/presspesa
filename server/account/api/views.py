from rest_framework import generics,status,views,permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer
from rest_framework.views import APIView
from firebase_admin import auth
from django.contrib.auth  import get_user_model

# Create your views here.

class RegisterUser(generics.GenericAPIView):
    def post(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if auth_header:
            id_token = auth_header.split(" ").pop()

            validate = auth.verify_id_token(id_token)

            if validate:
                user = get_user_model()
                get_user = user.objects.filter(username=validate['user_id']).first()

                if get_user:
                    data = {
                        'user_id': get_user.username,
                        'phone_number': get_user.phone_no
                    }
                    return Response({'data': data, 'message': 'Login seccessful'})
                else:
                    get_user = user(phone_no=validate['phone_number'], username=validate['user_id'])

                    get_user.save()
                    data = {
                        'user_id': get_user.username,
                        'phone_number': get_user.phone_no
                    }

                    return Response({'data': data, 'message': 'User created seccessful'})
            else:
               return Response({'message': 'invalid tokennn'})
        else:
               return Response({'message': 'token not provideddd'})


