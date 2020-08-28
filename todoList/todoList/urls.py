from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls,),
    path("", include("todo_main.urls", namespace="core")),
    path("index/", include("todo_main.urls", namespace="index")),
    path("home/", include("todo_main.urls", namespace="home")),
    # 게시판 앱
    path("board/", include("todo_board.urls")),
]
