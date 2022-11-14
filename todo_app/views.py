from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/index.html"
    paginate_by = 5
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo_app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo_app:index")

    def update_status(self):
        if self.model.status:
            self.model.status = False
        else:
            self.model.status = True


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo_app:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo/tags_list.html"
    paginate_by = 5
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_app:tag-list")


def complete_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if not task.status:
        task.status = True

    task.save()
    return HttpResponseRedirect(
        reverse_lazy("todo_app:index")
    )


def undo_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.status:
        task.status = False
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("todo_app:index")
    )
