from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
    return JsonResponse({'error': 'Invalid data'}, status=400)

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'id': task.id, 'completed': task.completed})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return JsonResponse({'id': pk})
