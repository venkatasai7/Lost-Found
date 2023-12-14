from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from .models import Tasks 
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import TaskForm


class  TaskListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'blog/home.html'
    context_object_name = 'Tasks'
    ordering =['CreatedDate']
    paginate_by = 4

class  UserTaskListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'blog/User_Tasks.html'
    context_object_name = 'Tasks'

    paginate_by = 4
    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Tasks.objects.filter(Owner = user).order_by('CreatedDate')

class  MyTaskListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'blog/My_Tasks.html'
    context_object_name = 'Tasks'

    paginate_by = 4
    def get_queryset(self):
        user =  self.request.user
        return Tasks.objects.filter(Owner = user).order_by('CreatedDate')


class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Tasks


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Tasks
    form_class = TaskForm
    

    def form_valid(self, form):
        form.instance.Owner = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Tasks
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.Owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self) :
        Task = self.get_object()
        if self.request.user == Task.Owner:
            return True
        else:
            return False

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Tasks 
    success_url = '/'
    def test_func(self) :
        Task = self.get_object()
        if self.request.user == Task.Owner:
            return True
        else:
            return False     