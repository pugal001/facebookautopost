from rest_framework import serializers
from common.models import Templates
import time


class TemplatesSerializer(serializers.ModelSerializer):
    sheduled = serializers.SerializerMethodField()
    def get_sheduled(self,obj):
       pass
    class Meta:
        model = Templates
        fields = '__all__'

