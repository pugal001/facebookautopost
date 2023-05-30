from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from Facebook.models import Details
from Facebook.api.serializers import DetailsSerializer
from django.shortcuts import render
import datetime
import time
from django.views.decorators.csrf import csrf_exempt    
from rest_framework.decorators import action
from rest_framework.response import Response


class Detailview(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'patch', 'retrieve', 'put']

    @action(detail=True, methods=['get'], url_path='get-post-details',)
    @csrf_exempt
    def get_post_details(self, request, *args, **kwargs):
        data = self.get_object()
        serialize = DetailsSerializer(instance=data,context={'request': request}).data       
        print(serialize['id'])

        import facebook
        # import pandas as pd

        token = serialize['API_key']
        page_post_id = serialize['facebook_id']
        graph = facebook.GraphAPI(access_token = token)
        posts = graph.get_object(id = page_post_id, fields = 'posts')
        data =[]
        for i in posts:
            if i == 'posts':
                post_data_details = posts[i]
                post_data=post_data_details['data']
                post_count = 0
                for datas in post_data:
                    
                    if 'message' in datas.keys():
                        comments = graph.get_object(id = datas["id"],fields = 'comments')
                        list_of_comments = []
                        if 'comments' in comments.keys():
                            comment_array = comments['comments']['data']
                            for comment in comment_array:
                                list_of_comments.append({'comment_data':comment['message'], 'commented_on':comment['created_time']})
                        else:
                            list_of_comments.append('no comments')
                        #print(f'count of the post{post_count},post_image_id: {datas["id"]} post_image_message: {datas["message"]}')
                        like = graph.get_object(id=datas["id"], fields='comments.limit(1).summary(true),likes.limit(1).summary(true)')
                        print(f'the posted comment got number of like is: {like["comments"]["summary"]["total_count"]}')
                        count = like["comments"]["summary"]["total_count"]
                        data.append({'record':post_count, 'details':f'post_image_id: {datas["id"]} post_image_message: {datas["message"]}', 'comments that post having is': list_of_comments,'count_of_likes':count})
                        print(comments)
                    post_count +=1
                    if 'story' in datas.keys():
                        
                        comments = graph.get_object(id = datas["id"],fields = 'comments')
                        list_of_comments = []
                        if 'comments' in comments.keys():
                            comment_array = comments['comments']['data']
                            for comment in comment_array:
                                list_of_comments.append({'comment_data':comment['message'], 'commented_on':comment['created_time']})
                        else:
                            list_of_comments.append('no comments')
                        #print(f'count of the post{post_count},posted_date: {datas["created_time"]} posted_detail: {datas["story"]}')   
                        print(f'the posted comment got number of like is: {like["comments"]["summary"]["total_count"]}')
                        count = like["comments"]["summary"]["total_count"]
                        data.append({'record':post_count, 'details':f'posted_date: {datas["created_time"]} posted_detail: {datas["story"]}','comments that post having is': list_of_comments,'count_of_likes':count})
                    
                    
                        print(comments)

        
        
        return Response(data)
    
    @action(detail=True, methods=['get'], url_path='post-images',)
    @csrf_exempt
    def get_post_images(self, request, *args, **kwargs):
        data = self.get_object()
        serialize = DetailsSerializer(instance=data,context={'request': request}).data       
        print(serialize)

        
        import requests
        page_id_1 = int(serialize['facebook_id'])
        facebook_access_token_1 = serialize["API_key"]
        image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
        image_location = "http://13.232.165.181:9000/aqua/product_images/shiva5.jpg"
        img_payload = {
        'url': image_location,
        'access_token': facebook_access_token_1
        }
        #Send the POST request
        r = requests.post(image_url, data=img_payload)
        print(r.text)
        return Response(r.text)
    
    @action(detail=True, methods=['get'], url_path='post-messages',)
    @csrf_exempt
    def get_post_messages(self, request, *args, **kwargs):
        data = self.get_object()
        serialize = DetailsSerializer(instance=data,context={'request': request}).data       
        print(serialize)

    
        import facebook

        groups = serialize['facebook_id']
        msg = "this is an automated python script message"
        link = ""
        token = serialize['API_key']
        graph = facebook.GraphAPI(access_token=token)
        x = graph.put_object(groups, 'feed', message = msg, link = link)
        print(x)
        return Response(x)
