from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "todo_board"

urlpatterns = [
    path("", views.TodoListBoard.as_view(), name="todo_board"),
    path("insert/", views.check_post, name="todo_board_insert"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
