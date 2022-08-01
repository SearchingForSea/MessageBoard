from calendar import c
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import AddressSecret
from .models import GetMessage
from .models import PraiseTread

class addressSecret(serializers.ModelSerializer):
    class Meta:
        model=AddressSecret
        fields=('User_Address','User_Secret')

class getMessage(serializers.ModelSerializer):
    class Meta:
        model=GetMessage
        fields=('User_Address','User_Comment','Comment_date')

class praiseTread(serializers.ModelSerializer):
    class Meta:
        model=PraiseTread
        fields=('User_Address','User_Comment','User_Comment_Tread','User_Comment_Praise')