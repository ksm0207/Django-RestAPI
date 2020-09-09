from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm
from datetime import datetime, timedelta
from django.views import generic


class TodoListBoardView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "todo_board/todo_list.html"
        # 기한 없는 일정 및 마감 안된 일정 불러오기
        todo_list_date_no = TodoList.objects.all().filter(end_date__isnull=True, is_complete=0).order_by('priority')
        print(todo_list_date_no)
        # 기한 있는 일정 및 마감이 안된 일정 불러오기
        todo_list_date_non_complete = TodoList.objects.all().filter(end_date__isnull=False, is_complete=0).order_by('priority')
        print(todo_list_date_non_complete)
        # 마감이 완료된 데이터 불러오기 is_complete 값이 1인 테이블을 찾고 완료된 값은 1
        todo_list_date_complete = TodoList.objects.all().filter(is_complete=1).order_by('end_date')
        print(todo_list_date_complete)
        today = datetime.now()
        # 마감일이 가까워지는 데이터를 담는 변수 설정
        close_end_day = []
        # 기한이 지난 데이터를 담는 변수 설정
        over_end_day = []

        for i in todo_list_date_non_complete:
            day = str(i.end_date).split("-")
            print(day)
            end_day = datetime(int(day[0]), int(day[1]), int(day[2]))
            print(end_day)
            if (end_day - today).days < - 1:
                over_end_day.append(i.title)
            if (end_day - today).days >= -1 and (end_day - today).days < 3:
                close_end_day.append(i.title)
        return render(request, template_name, {"todo_list_date_non_complete": todo_list_date_non_complete, "todo_list_date_complete": todo_list_date_complete, "todo_list_date_no": todo_list_date_no, 'close_end_day': close_end_day, 'over_end_day':over_end_day})
        # todo_list = TodoList.objects.all()
        # return render(request, template_name, {"todo_list": todo_list})


class TodoDetailView(generic.DetailView):
    model = TodoList
    template_name = "todo_board/todo_board_detail.html"
    context_object_name = "todo_list"


class TodoUpdateView(generic.UpdateView):
    model = TodoList
    fields = ("title", "content", "end_date")
    template_name = "todo_board/todo_board_update.html"
    success_url = "/board/"

    def form_valid(self, form):
        form.save()
        return render(
            self.request,
            "todo_board/todo_board_success.html",
            {"message": "일정 업데이트 완료"},
        )

    def get(self, request, *args, **kwargs):
        # 오브젝트를 받아와서 폼 클래스를 받아온후 값을 리턴해야함
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


class TodoDeleteView(generic.DeleteView):
    model = TodoList
    template_name = "todo_board/todo_board_delete.html"
    success_url = "/board/"
    context_object_name = "todo_list"


def check_post(request):
    template_name = "todo_board/todo_board_success.html"
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정을 추가하였습니다"
            return render(request, template_name, {"message": message,})
    else:
        template_name = "todo_board/todo_board_insert.html"
        form = TodoForm
        return render(request, template_name, {"form": form})

