from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import TodoForm
from .models import TodoItem

# list todos
def todos(request):

    context = {
        'todos': TodoItem.objects.all(),
    }
    return render(request, "todos.html", context)

# todo form
def todo_form(request, pk=None):
    if request.method == "POST":
        if pk:
            todo = get_object_or_404(TodoItem, pk=pk)
            form = TodoForm(request.POST, instance=todo)

        else:
            form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("todos")  
    
    else:
        if pk:
            todo = get_object_or_404(TodoItem, pk=pk)
            form = TodoForm(instance=todo)

        else:
            form = TodoForm()

    context = {
        'form': form  
    }

    return render(request, "todo_form.html", context)

# details for a single todo
def todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    context = { 'todo': todo }

    change_status = request.GET.get('change_status', None)

    if change_status:
        todo.is_done = True
        todo.save()
    
    return render(request, "todo.html", context)

def delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return redirect("todos")

