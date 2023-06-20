from django.urls import path
from .views import (
    home,
    student,
    student_detail,
    student_add,
    StudentAddView,
    )



urlpatterns = [
    path('',home),
    path('student/', student),
    path('detail/', student_detail,name='list'),
    path('add/', student_add,name='add'),
    path('student-add/', StudentAddView.as_view(), name='student-add'),
]

