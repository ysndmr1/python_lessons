from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

from .forms import (
    Todo, TodoForm
)

# ------------------------------------
# Function Based Views
# ------------------------------------

# List:
def todo_list(request):
    return render(request, 'list.html', {
        "todos": Todo.objects.all()
    })


# Add:
def todo_add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Message:
        messages.success(request, 'Kaydedildi.')
        # If OK redirect:
        return redirect('todo_list') # redirect('path_name')
    context = {
        "form": form
    }
    # return render(request, 'add.html', context)
    return render(request, 'add_update.html', context)


# Update:
def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method== "POST":
        form = TodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Güncellendi.')
            return redirect("todo_list")
    context = {
        'form': form,
        'todo': todo
    }
    # return render(request, 'update.html', context)
    return render(request, 'add_update.html', context)

# Delete:
def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Silindi.')
    # No need template.
    return redirect("todo_list")