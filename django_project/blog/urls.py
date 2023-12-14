from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,TaskDeleteView,UserTaskListView,MyTaskListView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(),name = 'blog-blog_home'),
    path('user/<str:username>', UserTaskListView.as_view(),name = 'User-Tasks'),
    path('Mytasks', MyTaskListView.as_view(),name = 'MyTasks'),
    path('Task/<int:pk>/', TaskDetailView.as_view(),name = 'Task-Detail'),
    path('Task/new/', TaskCreateView.as_view(),name = 'Task-Create'),
    path('Task/<int:pk>/update', TaskUpdateView.as_view(),name = 'Task-Update'),
    path('Task/<int:pk>/delete', TaskDeleteView.as_view(),name = 'Task-Delete'),
    
    
]