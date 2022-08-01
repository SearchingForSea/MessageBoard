
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


# Create your views here.

# class users_data_view(viewsets.ModelViewSet):
#     queryset = AddressSecret.objects.all()
#     serializer_class = addressSecret

def registerUser(request):
#    user_address = request.GET.get(user_address,'' )
#    user_secret = request.GET.get(‘age’, 0)
#    secret=AddressSecret.objects.filter(User_Address=user_address)
#    if secret==user_secret:
#    address=models.AddressSecret.objects.create(User_Address='1',User_Address='2')
#    print(address)
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

    

# def loginUser(request,user_address,user_secret):
#    secret=AddressSecret.objects.filter(User_Address=user_address)
#    if secret==user_secret:
#        return HttpResponse('Yes')
#    else: return HttpResponse('no')

# def getPraiseTread(request,user_address):
#     result=PraiseTread.objects.all()
#     return result

# def changPraise(request,user_address):
#     user_message = PraiseTread.objects.get(User_Address=user_address)
#     user_message.User_Comment_Praise='1'

# def changTread(request,user_address):
#     user_message = PraiseTread.objects.get(User_Address=user_address)
#     user_message.User_Comment_Tread='1'

# def sendMessage(requset,user_address,message):
#     PraiseTread.objects.create(User_Address=user_address,User_Comment=message,
#     User_Comment_Tread='0',User_Comment_Praise='0')

