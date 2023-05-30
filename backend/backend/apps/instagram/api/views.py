from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from instagram.models import InstaUser
from instagram.api.serializers import InstagramSerializer, InstagramPostSerializer, SearchHistorySerializer, FollowersSerializer
from django.shortcuts import render
import datetime
import time
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response


class InstauserViews(viewsets.ModelViewSet):
    queryset = InstaUser.objects.all()
    serializer_class = InstagramSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']

    @action(detail=True, methods=['get'], url_path='post-datas',)
    @csrf_exempt
    def post_datas(self, request, *args, **kwargs):
        data = self.get_object()
        result = InstagramPostSerializer(instance=data, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-topsearches',)
    @csrf_exempt
    def topsearches(self, request, *args, **kwargs):
        data = self.get_object()
        result = SearchHistorySerializer(instance=data, context={'request': request}).data
        return Response({"result": result})

    @action(detail=True, methods=['get'], url_path='get-follows',)
    @csrf_exempt
    def follows(self, request, *args, **kwargs):
        data = self.get_object()
        result = FollowersSerializer(instance=data, context={'request': request}).data
        return Response({"result": result})
