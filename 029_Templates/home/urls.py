from django.urls import path
from .views import home,student,student_detail


urlpatterns = [
    path('',home),
    path('student/', student),
    path('detail/', student_detail),
]
