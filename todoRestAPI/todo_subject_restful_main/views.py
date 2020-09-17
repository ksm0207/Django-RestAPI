# from django.shortcuts import render
from .serializers import TodoSerializer, TodoDetailSerializer
from .models import TodoList

# from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


# ListView
class TodoMainView(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


# DetailView
class TodoRestDetailView(RetrieveAPIView):
    lookup_field = "no"
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer


# UpdateView
class TodoRestUpdateView(UpdateAPIView):
    lookup_field = "no"
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


# DeleteView
class TodoDeleteView(DestroyAPIView):
    lookup_field = "no"
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
