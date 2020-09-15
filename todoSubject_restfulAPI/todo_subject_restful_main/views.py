from django.shortcuts import render
from .models import TodoList
from .serializers import TodoSerializer
from rest_framework import viewsets


class TodoMainView(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
