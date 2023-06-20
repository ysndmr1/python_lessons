from django.urls import path
from .views import (
    home,
    student,
    student_detail,
    student_add,
    StudentAddView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
    )



urlpatterns = [
    path('',home),
    path('student/', student),
    path('detail/', student_detail,name='list'),
    path('add/', student_add,name='add'),
    path('student-add/', StudentAddView.as_view(), name='student-add'),
    path('student-list/', StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
]

