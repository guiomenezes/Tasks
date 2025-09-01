from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tasks
from .forms import TasksForm

# Create your views here.

@login_required
def tasks(request):
    # Filtra apenas as tarefas do usuário logado
    user_tasks = Tasks.objects.filter(user=request.user).order_by('-date', '-id')
    data = {'data': user_tasks}
    return render(request, 'tasks/tasks_page.html', context=data)

@login_required
def create_task(request):
    if request.method == 'POST':
        task_form = TasksForm(request.POST)
        if task_form.is_valid():
            # Salva a tarefa associanado ao usuário logado
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('tasks')
    else:
        task_form = TasksForm()
    form = {'form': task_form}
    return render(request, 'tasks/new_task_page.html', context=form)

@login_required
def edit(request, id_task):
    # Garante que o usuário só pode editar suas próprias tarefas
    task = get_object_or_404(Tasks, pk=id_task, user=request.user)
        
    if request.method == 'GET':
        form = TasksForm(instance=task)
        return render(request, 'tasks/new_task_page.html', {'form':form})
    else:
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
        return redirect('tasks')

@login_required
def delete(request, id_task):
    # Garante que o usuário só pode deletar suas próprias tarefas
    task = get_object_or_404(Tasks, pk=id_task, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('tasks')
    return render(request, 'tasks/delete_page.html', {'item': task})