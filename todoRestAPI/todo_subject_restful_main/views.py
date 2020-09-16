# from django.shortcuts import render
from .serializers import TodoSerializer
from .models import TodoList
from rest_framework import viewsets


class TodoMainView(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

