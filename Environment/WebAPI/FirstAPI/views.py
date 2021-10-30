from django.db.models import query
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Person
from .serializer import PersonSerializers
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class PersonViewPagenation(LimitOffsetPagination):
    max_limit = 3
    default_limit = 2

class PersonView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('Name', 'Age')
    search_fields = ('id', 'Name')
    pagination_class =  PersonViewPagenation
    
class PersonCreateListAPI(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    def create(self, request, *args, **kwargs):
        try:
            Name = request.data.get("Name",None)
            Age = request.data.get("Age",None)
            BirthDays = request.data.get("BirthDays",None)
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                "Message":"Failed"
            })


# class PersonView(APIView):
#     def get(ser)

# class PersonView(APIView):
#     def get(self, request, format= None):
#         data= Person.objects.all()
#         serializer = PersonSerializers(data, many = True)
#         return Response(serializer.data)
#     def post(self,request,format= None):

#         try:

#             serializer = PersonSerializers(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)

#         except Exception as e:
#             return Response(serializer.errors)

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
