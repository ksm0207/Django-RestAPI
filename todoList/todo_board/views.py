from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm
from django.views import generic
from django.http import JsonResponse
from datetime import datetime, timedelta
import json


class TodoListBoardView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        # Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = "todo_board/todo_list.html"
        # 기한 없는 일정, 마감 안된 애들
        todo_list_no_endDate = (
            TodoList.objects.all()
            .filter(end_date__isnull=True, is_complete=0)
            .order_by("priority")
        )
        print("기한 없는 일정 및 마감이 안된 데이터 :", todo_list_no_endDate)

        # 기한 있고, 마감이 안된 애들
        todo_list_endDate_non_complete = (
            TodoList.objects.all()
            .filter(end_date__isnull=False, is_complete=0)
            .order_by("priority")
        )
        print("기한 있고 마감이 안된 데이터 : ", todo_list_endDate_non_complete)

        # 마감이 된 애들
        todo_list_endDate_complete = (
            TodoList.objects.all().filter(is_complete=1).order_by("end_date")
        )
        print("마감이 완료된 데이터:", todo_list_endDate_complete)
        today = datetime.now()

        # 마감일이 가까워지는날인 변수
        close_end_day = []

        # 마감날이 지난 변수
        over_end_day = []

        for i in todo_list_endDate_non_complete:
            e_day = str(i.end_date).split("-")
            end_day = datetime(int(e_day[0]), int(e_day[1]), int(e_day[2]))
            if (end_day - today).days < -1:
                over_end_day.append(i.title)
                print("마감날이 지난 데이터 over end day :", over_end_day)
            if (end_day - today).days >= -1 and (end_day - today).days < 3:
                close_end_day.append(i.title)
                print("마감일이 가까워지는 데이터 : ", close_end_day)
        return render(
            request,
            template_name,
            {
                "todo_list_endDate_non_complete": todo_list_endDate_non_complete,
                "todo_list_endDate_complete": todo_list_endDate_complete,
                "todo_list_no_endDate": todo_list_no_endDate,
                "close_end_day": close_end_day,
                "over_end_day": over_end_day,
            },
        )
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
        if str(request.path).split("/board/")[1].split("/")[0] == "insert":
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.todo_save()
                message = "일정을 추가하였습니다"
                return render(request, template_name, {"message": message})
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_complete":
            pk = request.POST["data"]
            return_value = checkbox_event(pk, True)
            return JsonResponse(return_value)
        elif str(request.path).split("/board/")[1].split("/")[0] == "is_non_complete":
            pk = request.POST["data"]
            return_value = checkbox_event(pk, False)
            return JsonResponse(return_value)
    else:
        template_name = "todo_board/todo_board_insert.html"
        form = TodoForm
        return render(request, template_name, {"form": form})


def checkbox_event(pk, is_check):
    todo_selected = TodoList.objects.get(pk=pk)
    if is_check == True:
        todo_selected.is_complete = 1
        todo_selected.priority = None
    else:
        todo_selected.is_complete = 0
    todo_selected.save()
    return_value = {"text": "저장되었습니다."}
    return return_value
