from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.PersonView.as_view()),
    path('add/',views.PersonCreateListAPI.as_view()),
]
