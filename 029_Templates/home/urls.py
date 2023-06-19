from django.urls import path
from .views import home,student


urlpatterns = [
    path('',home),
    path('student/', student)
]
