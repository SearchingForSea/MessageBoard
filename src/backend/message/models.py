from pyexpat import model
from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
#取密码,储存账号密码
class AddressSecret(models.Model):
    User_Address=models.CharField(max_length=10)
    User_Secret=models.CharField(max_length=10)

#取评论
class GetMessage(models.Model):
    Comment_Bool=models.BooleanField(default=True)
    User_Address=models.CharField(max_length=10)
    User_Comment=models.CharField(max_length=300)

#赞和踩
class PraiseTread(models.Model):
    User_Address=models.CharField(max_length=10)
    User_Comment=models.CharField(max_length=300)
    User_Comment_Tread=models.CharField(max_length=1)
    User_Comment_Praise=models.CharField(max_length=1)

