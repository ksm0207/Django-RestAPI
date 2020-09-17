# from django.shortcuts import render
from .serializers import TodoSerializer, TodoDetailSerializer
from .models import TodoList

# from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView


class TodoMainView(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


class TodoRestDetailView(RetrieveAPIView):
    lookup_field = "no"
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer

