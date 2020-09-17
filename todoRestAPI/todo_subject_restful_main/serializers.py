from .models import TodoList
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ("no", "title", "content", "is_complete", "end_date", "priority")


# 디테일용 Serializer
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ("no", "title", "content", "is_complete", "end_date", "priority")


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ("title", "content", "end_date")

