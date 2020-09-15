from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "todo_board"

urlpatterns = [
    path("", views.TodoListBoardView.as_view(), name="todo_board"),
    path("insert/", views.check_post, name="todo_board_insert"),
    path("is_complete/$", views.check_post, name="todo_board_is_complete"),
    path("is_non_complete/$", views.check_post, name="todo_board_is_non_complete"),
    path("save_prioirity/$", views.check_post, name="todo_board_save_priority"),
    path("detail/<int:pk>", views.TodoDetailView.as_view(), name="todo_board_detail"),
    path("update/<int:pk>", views.TodoUpdateView.as_view(), name="todo_board_update"),
    path("delete/<int:pk>", views.TodoDeleteView.as_view(), name="todo_board_delete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
