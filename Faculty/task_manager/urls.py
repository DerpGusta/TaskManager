"""urls module"""

from django.urls import path
from task_manager import views
from .views import (TaskListView, TaskCreateView, TaskDetailView,
                    TaskUpdateView, TaskDeleteView, load_metrics)

urlpatterns = [
    path('', TaskListView.as_view(), name='task'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('ajax/load_metrics/', load_metrics, name='ajax_load_metrics')
]
