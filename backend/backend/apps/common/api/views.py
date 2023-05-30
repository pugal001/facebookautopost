from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from common.models import Templates
from common.api.serializers import TemplatesSerializer
from django.shortcuts import render
import datetime
import time


class templateview(viewsets.ModelViewSet):
    queryset = Templates.objects.all()
    serializer_class = TemplatesSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']


def templateviews(request):
    # def digital_clock():
    #     while True:
    #         time.sleep(1)
    #         current_time = datetime.datetime.now()
    #         return current_time
    
    # clock = digital_clock   
    # #clock = '8.00'
    
    data = Templates.objects.all()
    serialize = TemplatesSerializer(data, many=True).data  
    for i in serialize:
        data = i['template_image']  
    mydict = {'time':data}
    
    
    return render(request, 'basic.html', context=mydict)