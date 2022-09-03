
import json
from unittest import result
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import AddressSecret
from .models import GetMessage
from .models import PraiseTread
from .serializers import addressSecret
from .serializers import getMessage
from .serializers import praiseTread
from django.http import JsonResponse
from message import models
from django.core import serializers

def registerUser(request):
    if request.method=='POST':
        user_address1 = request.POST.get('user_address', 'nouser')
        user_secret1 = request.POST.get('user_secret', 'noposs')
        try:
            object = AddressSecret.objects.get(User_Address=user_address1)
            return HttpResponse("no")
        except:
            AddressSecret.objects.create(User_Address=user_address1,User_Secret=user_secret1)
            return HttpResponse("Yes")

def loginUser(request):
    if request.method=='POST':
        user_address1 = request.POST.get('user_address', 'nouser')
        user_secret1 = request.POST.get('user_secret', 'noposs')
        try:
            object = AddressSecret.objects.get(User_Address=user_address1)
            GetMessage.objects.create(Comment_Bool=True,User_Address=user_address1,User_Comment="")
            secret=object.User_Secret
            if secret==user_secret1:
                return HttpResponse("Yes")
            else:
                return HttpResponse("no")
        except:
            return HttpResponse("no")

def sendMessage(request):
    if request.method=='POST':
        user_address=request.POST.get('user_address','haha')
        talk_message=request.POST.get('talk','')
        PraiseTread.objects.create(User_Address=user_address,
        User_Comment=talk_message,User_Comment_Tread='0',User_Comment_Praise='0')
        return HttpResponse("Yes")

def getMessage(request):
    if request.method=='POST':
        # talkcomment=PraiseTread.objects.all().values()
        # return HttpResponse(talkcomment)
        talkcomment=PraiseTread.objects.all()
        talkcomment_reverse=talkcomment[::-1]
        data=serializers.serialize('json',talkcomment_reverse,ensure_ascii=False)
        return HttpResponse(data)

def getAddress(request):
    if request.method=='POST':
        try:
            getUserAddress=GetMessage.objects.last()
            data=getUserAddress.User_Address
            return HttpResponse(data)
        except:
            return HttpResponse('')


