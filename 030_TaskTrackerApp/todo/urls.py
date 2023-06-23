from django.urls import path, include

from .views import (
    # FBV:
    todo_list,
    todo_add,
    todo_update,
    todo_delete,
)

# after '/':
urlpatterns = [
   # FBV:
    # path('list/', todo_list, name='todo_list'),
    # path('add/', todo_add, name='todo_add'),
    # path('update/<int:pk>', todo_update, name="todo_update"),
    # path('delete/<int:pk>', todo_delete, name="todo_delete"),
]