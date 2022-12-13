from django.test import TestCase as DjangoTestCase
from django.contrib.auth.models import User
from tweets.models import Tweet

class TestCase(DjangoTestCase):
    def createUser(self,username,email,password=None):
        if password is None:
            password = "test123"
        return User.objects.create_user(username,email,password)
    def createTweet(self,user,content=None):
        if content is None:
            content = 'default tweet content'
        return Tweet.objects.create(user=user,content=content)