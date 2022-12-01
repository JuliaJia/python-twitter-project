from django.db import models


class User(models.Model):
    user_id = models.TextField(default=0)

class Photo(models.Model):
    Photo_id = models.TextField(default=0)


class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(Photo,blank=True)
    likes_count = models.BigIntegerField(default=0,null=True)
    comments_count = models.BigIntegerField(default=0,null=True)



class Tweet_user(models.Model):
    user = models.CharField(max_length=200,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.BigIntegerField(default=0,null=True)
    comments_count = models.BigIntegerField(default=0,null=True)

