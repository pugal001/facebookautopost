from rest_framework import serializers
from Facebook.models import Details
import time



class DetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Details
        fields = '__all__'

    
    def create(self, validated_data):
        print(validated_data)
        detail = Details.objects.create(facebook_id=validated_data['facebook_id'],
                                        name = validated_data['name'],
                                        email = validated_data['email'],
                                        data = validated_data['data'],
                                        message=validated_data['message'])
        
        
        return detail
    def update(self, instance, validated_data):
        instance.facebook_id = validated_data.get('facebook_id', instance.facebook_id)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.data = validated_data.get('data', instance.data)
        instance.message = validated_data.get('message', instance.message)
        instance.API_key = validated_data.get('API_key', instance.API_key)
        instance.save()
        return instance
        




        #basic own api passing
        # import facebook
        # from facebook import GraphAPI
        # token = 'EAADVUoTReF8BAF23dMlHOuHvfyUdh8rQiaQigfetZANfmSEhgU45zxPqtz4g0ipFG1UZC16ATsTZBvZC2DzaVGjJb3dVZCZBWAi7LqJ6xdJRf4jE7BfrZAZCzgAtUESpBy0Ibf95XWH1H39xZAzcNERYXZBjiUm3kw4ynHRduei4AdaZCyZBc8PhsK09'

        # graph = facebook.GraphAPI(access_token=token, version = 3.1)
        # events = graph.request('me?fields=id,name,email,posts,photos,gender')

        # print(events) 
        # return detail 
