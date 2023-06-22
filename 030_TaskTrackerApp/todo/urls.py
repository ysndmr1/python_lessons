from django.urls import path, include

from .views import (
    # FBV:
    todo_list,
)

# after '/':
urlpatterns = [
    path('list/', todo_list),
]