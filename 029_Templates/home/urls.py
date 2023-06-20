from django.urls import path
from .views import (
    home,
    student,
    student_detail,
    student_add
    )



urlpatterns = [
    path('',home),
    path('student/', student),
    path('detail/', student_detail,name='list'),
    path('add/', student_add,name='add'),
]

