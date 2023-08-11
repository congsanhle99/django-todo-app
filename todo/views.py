from django.http import HttpResponse
from django.shortcuts import render
from todoApp.models import Task


def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by("-update_at")
    completedTasks = Task.objects.filter(
        is_complete=True).order_by("-update_at")
    context = {"tasks": tasks, "completedTasks": completedTasks}
    return render(request, 'home.html', context)
