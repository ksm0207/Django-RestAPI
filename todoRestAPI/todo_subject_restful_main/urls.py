from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# from rest_framework import routers

app_name = "todo_subject_restful_main"

# routers = routers.DefaultRouter()
# routers.register(r"todo_board", views.TodoMainView)
urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", views.TodoMainView.as_view(), name="todo_list"),
    url(r'^todo_list/(?P<no>\d+)/$', views.TodoRestDetailView.as_view(), name='todo_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

