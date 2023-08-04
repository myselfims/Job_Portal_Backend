from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.


def home(request):
    return HttpResponse('hello')

    
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    