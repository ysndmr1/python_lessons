from django.urls import path

from .views import (
    # FBV:
    todo_list,
    todo_add,
    todo_update,
    todo_delete,
    # CBV:
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
)

# after '/':
urlpatterns = [
    # FBV:
    # path('list/', todo_list, name='todo_list'),
    # path('add/', todo_add, name='todo_add'),
    # path('update/<int:pk>', todo_update, name="todo_update"),
    # path('delete/<int:pk>', todo_delete, name="todo_delete"),
    # CBV:
    path('list/', TodoListView.as_view(), name='todo_list'),
    path('add/', TodoCreateView.as_view(), name='todo_add'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),
]
