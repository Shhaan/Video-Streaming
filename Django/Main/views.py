from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings 
from .producer import publish
# Create your views here.
  
class Home(APIView): 
    def get(self, request):    
        publish('list',{'name':'baba'})
        return Response('hi')    
    
      