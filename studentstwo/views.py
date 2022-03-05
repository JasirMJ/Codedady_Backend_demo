from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.

class StudentAPITwo(ListAPIView):
    def post(self,request):
        print(self.request.data)

        for x in self.request.data:
            print(x.value)

        return Response({
            "Message" : "Success"
        })