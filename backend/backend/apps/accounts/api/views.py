from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import copy
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from accounts.models import User, create_username
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from accounts.api.serializers import UserRegistrationSerializer, UserBasicInfoSerializer, UserProfileInfoSerializer
from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings


@csrf_exempt
def logout_View(request):
    logout(request)
    return HttpResponse("logout successful")


@api_view(['post', ])
@csrf_exempt
@permission_classes([AllowAny])
@authentication_classes([])
def user_login_view(request):

    if request.method == 'POST':
        data = request.data
        user = authenticate(request, email=data['email'], password=data['password'])
        user_data = {}
        if user is not None:
            login(request, user)
            user_data = UserBasicInfoSerializer(instance=user).data
            return Response(user_data)
        else:
            user_data['message'] = "login failed"
            return Response(user_data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['post', 'patch'])
@csrf_exempt
def user_registration_view(request):

    if request.method == 'POST':
        serialize = UserRegistrationSerializer(data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['response'] = "Successfully registered a new user."
            data['id'] = user.id
            data['email'] = user.email
            data['phone_no'] = user.phone_no
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            data['is_verified'] = user.is_verified
           
        else:
            data = serialize.errors
        return Response(data)


@api_view(['post', 'get'])
@csrf_exempt
def user_terms_accept(request):
    if request.method == 'POST':
        dic = request.data
        mail = dic['email']
        filtering = User.objects.filter(email = mail)
        filtering.update(is_terms_accepted = True)
        user = UserProfileInfoSerializer(filtering, many=True).data
        return Response(user)
    elif request.method == 'GET':
        email = request.META['HTTP_AQUA_AUTH_TOKEN']
        data = User.objects.filter(email = email)
        serialize = UserProfileInfoSerializer(data, many=True).data
        return Response(serialize)


class user_profile_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileInfoSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']


