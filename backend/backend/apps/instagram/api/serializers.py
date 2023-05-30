from rest_framework import serializers
from instagram.models import InstaUser
import time
import instaloader
import pandas as pd
import re
import instaloader
import pandas as pd
from instagrapi import Client
from instagrapi.types import Usertag, Location


class InstagramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InstaUser
        fields = ['insta_user_name', 'password', 'image']

    def create(self, validated_data):
        print(validated_data)
        # Creating an instance of the Instaloader class
        bot = instaloader.Instaloader()

        # Loading a profile from an Instagram handle
        
        profile = instaloader.Profile.from_username(bot.context, validated_data['insta_user_name'])
        print(profile)
        try:
            insta_intance = InstaUser.objects.create(
                insta_user_name = profile.username,
                insta_user_id = profile.userid[0:4],
                number_of_posts =  profile.mediacount,
                followers_count = profile.followers,
                following_count = profile.followees,
                biography = profile.biography,
                external_url = profile.external_url,
                email=re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography),
                image = validated_data['image'],
                password = validated_data['password']
                )
            
            return insta_intance
        except:
            return "no user founded"

class InstagramPostSerializer(serializers.ModelSerializer):
    
    posts = serializers.SerializerMethodField()

    def get_posts(self,obj):
        data = InstaUser.objects.filter(id= obj.id).values()
        name = data[0]["insta_user_name"]       

        insta_username = obj.insta_user_name
        password = obj.password

        cl = Client()
        cl.login(insta_username, password)

        #user = cl.user_info_by_username("python code check")
        media = cl.photo_upload(
            path = "grass.jpg",
            caption = "wakanda forever i am ironman",
            #usertags=[Usertag(user=user, x=0.5, y=0.5)],
            location=Location(name="Spain,Madrid", lat=40.415390,lng=3.684243),
            #disabling extra options such as likes and comments
            extra_data={
                "custom_accessibility_caption":  "alternate texting example",
                "like_and_view_counts_disabled":False,
                "disable_comments":False
            }

        )

        return 'image  posted successfully'

    class Meta:
        model = InstaUser
        fields = ['posts']


class SearchHistorySerializer(serializers.ModelSerializer):
    
    searches = serializers.SerializerMethodField()

    def get_searches(self,obj):
        import instaloader

        # Creating an instance of the Instaloader class
        bot = instaloader.Instaloader()

        # Provide the search query here
        search_results = instaloader.TopSearchResults(bot.context, 'music')

        user_names = []
        search_history = []
        search_details = {}
        # Iterating over the extracted usernames
        for username in search_results.get_profiles():
            
            user_names.append(str(username))

        # Iterating over the extracted hashtags
        for hashtag in search_results.get_hashtags():
            search_history.append(str(hashtag))

        for name,search in zip(user_names, search_history):
            search_details[name] = search
        #print()    

        return search_details 

    class Meta:
        model = InstaUser
        fields = ['searches']


class FollowersSerializer(serializers.ModelSerializer):
    
    searches = serializers.SerializerMethodField()

    def get_searches(self,obj):
        data = InstaUser.objects.filter(id= obj.id).values()
        name = data[0]["insta_user_name"]
        #password = data[0]["password"]

        # Creating an instance of the Instaloader class
        bot = instaloader.Instaloader()
        bot.login(user='pugal_m23', passwd='pugal@001')

        # Loading a profile from an Instagram handle
        #once after you logged in you can give any account name get that account followers and following list
        profile = instaloader.Profile.from_username(bot.context, name)

        # Retrieving the usernames of all followers
        follower_list = []
        for follower in profile.get_followers():
            follower_list.append(follower.username)
        
        following_list = []
        # Retrieving the usernames of all followings
        for followee in profile.get_followees():
            following_list.append(followee.username)
        # Converting the data to a DataFrame
        result = {'list of followers':follower_list, 'list of following': following_list}

        return result 

    class Meta:
        model = InstaUser
        fields = ['searches']





        '''bot = instaloader.Instaloader()
bot.login(user="Pugal_m23",passwd="Cn1qo3mvrm#0")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'Pugal_m23')

# Retrieving all posts in an object
posts = profile.get_posts()

# Iterating and downloading all the individual posts
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")'''