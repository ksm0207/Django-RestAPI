from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm
from django.views import generic


class TodoListBoard(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "todo_board/todo_list.html"
        todo_list = TodoList.objects.all()
        print(todo_list)
        return render(request, template_name, {"todo_list": todo_list})


class TodoDetail(generic.DetailView):
    model = TodoList
    template_name = "todo_board/todo_board_detail.html"
    context_object_name = "todo_list"


def check_post(request):
    template_name = "todo_board/todo_board_success.html"
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정을 추가하였습니다"
            return render(request, template_name, {"message": message, })
    else:
        template_name = "todo_board/todo_board_insert.html"
        form = TodoForm
        return render(request, template_name, {"form": form})

