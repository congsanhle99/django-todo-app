from django.http import HttpResponse
from django.shortcuts import render
from todoApp.models import Task


def home(request):
    tasks = Task.objects.filter(is_complete=False)
    print(tasks)
    context = {"tasks": tasks}
    return render(request, 'home.html', context)
