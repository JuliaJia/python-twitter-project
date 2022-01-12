from django.contrib import admin
from accounts.models import Tweet_user

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','content','created_at','likes_count','comments_count')

admin.site.register(Tweet_user,TweetAdmin)

