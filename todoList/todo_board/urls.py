from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "todo_board"

urlpatterns = [
    path("", views.TodoListBoard.as_view(), name="board"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
