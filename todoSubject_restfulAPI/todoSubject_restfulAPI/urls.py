from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo_subject_restful_main.urls")),
]
