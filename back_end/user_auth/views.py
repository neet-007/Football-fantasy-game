from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserModelSerializer
import logging

logger = logging.Logger(__name__)
user_model = get_user_model()
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if not data.get('email'):
            return Response({'error':'email field is reqiured'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('password'):
            return Response({'error':'password field is reqiured'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('re_password'):
            return Response({'error':'re_password field is reqiured'}, status=status.HTTP_400_BAD_REQUEST)

        email = data['email']
        password = data['password']
        re_password = data['re_password']

        if len(password) < 8:
            return Response({'error':'password should be atleast 8 charecters long'}, status=status.HTTP_400_BAD_REQUEST)
        if password != re_password:
            return Response({'error':'password should be the same as re_password'}, status=status.HTTP_400_BAD_REQUEST)

        if user_model.objects.filter(email=email).exists():
            return Response({'error':'email is taken'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = user_model.objects.create_user(email, password)
        except Exception as e:
            logging.error('registring error with execption %s', e)
            return Response({'error':'an error occured please try agin'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logging.info('user was created with pk %d and email %s', user.pk, user.email)
        return Response({'success':'user is successfully created'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        if not data.get('email'):
            return Response({'error':'email field is reqiured'}, status=status.HTTP_400_BAD_REQUEST)

        if not data.get('password'):
            return Response({'error':'password field is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=data['email'], password=data['password'])
        if user is None:
            return Response({'error':'user with provided credintials not found'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            login(request, user)
        except Exception as e:
            logging.error('login error with exepction %s', e)
            return Response({'error':'an error occured please try again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success':'user successfully logged in'}, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
        except Exception as e:
            logging.error('logout error with exceotion %s', e)
            return Response({'error':'an error occured please try later'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success':'user logged out successfully'}, status=status.HTTP_200_OK)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    def get(self, request):
        return Response({'success':'csfrtoken generated'}, status=status.HTTP_200_OK)

class CheckUserView(APIView):
    def get(self, request):
        if request.user == AnonymousUser or not request.user:
            return Response({'error':'user is not authenticated'}, status=status.HTTP_200_OK)
        return Response({'success':UserModelSerializer(request.user).data}, status=status.HTTP_200_OK)


