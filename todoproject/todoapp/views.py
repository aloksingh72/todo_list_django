from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request,'todo/task_list.html',{"tasks":task,"form":form})


def delete_task(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('task_list')


def mark_completed(request,task_id):
    task = Task.objects.get(id = task_id)
    task.completed = 'True'
    task.save()
    return redirect('task_list')



