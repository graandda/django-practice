from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    complete_task_status,
    undo_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "task/<int:pk>/complete_task_status/",
        complete_task_status,
        name="complete-task-status",
    ),
    path(
        "task/<int:pk>/undo_task_status/",
        undo_task_status,
        name="undo-task-status",
    ),
]

app_name = "todo_app"
