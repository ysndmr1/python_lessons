from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello Python!</h1>')



def student(request):
    context= {
        'first_name':'Jacop',
        'my_list': [2020,2021,2022], 
        'book_name': 'lord of the rings',    
              }
    return render(request, 'home/home.html',context )

def student_detail(request):
    return render(request, 'home/student_detail.html')