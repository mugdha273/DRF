from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import Person
from rest_framework.response import Response
from .serializer import PersonSerializers

class PersonView(APIView):
    def get(self, request, format= None):
        data= Person.objects.all()
        serializer = PersonSerializers(data, many = True)
        return Response(serializer.data)
    def post(self,request,format= None):
        
        try:

            serializer = PersonSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
            
        except Exception as e:
            return Response(serializer.errors)

# Create your views here.
# global data
# data= ["Mugdha"]

# class Youtube(APIView):
                
#     def get(self,requests, format= None):
#         return Response({"Message" : data})
    
#     def post(self, requests, format= None):
#         Mydata= requests.data
#         Name = Mydata.get("Name", None)
#         data.append(Name)
#         print("Data Recieved: {}". format(data))
        
#         return Response(
#             {
#                 'Response': 200,
#                 "Data": Name,
#                 'Message': "It was added to the database"
#             }
#         )