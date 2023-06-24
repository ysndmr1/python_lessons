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


# ------------------------------------
# Class Based Views
# ------------------------------------
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

class TodoListView(ListView):
    model = Todo
    ordering = ['-id']
    # template_name = 'todo_list.html' # after 'templates/' default: 'modelname/modelname_list.html'



class TodoDetailView(DetailView):
    model = Todo
    # template_name = 'todo_detail.html' # after 'templates/' default: 'modelname/modelname_detail.html'


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_form.html' # after 'templates/' default: 'modelname/modelname_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Kaydedildi.')
        return super().post(request, *args, **kwargs)


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_form.html' # after 'templates/' default: 'modelname/modelname_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Güncellendi.')
        return super().post(request, *args, **kwargs)


class TodoDeleteView(DeleteView):
    model = Todo
    # form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    # template_name = 'todo_confirm_delete.html' # after 'templates/' default: 'modelname/modelname_confirm_delete.html'

    # template dosyasına git, onay al, öyle sil:
    # def post(self, request, *args, **kwargs):
    #     messages.success(request, 'Silindi.')
    #     return super().post(request, *args, **kwargs)
    
    # template dosyasına gitmeden direkt sil:
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Silindi.')
        return super().delete(request, *args, **kwargs)