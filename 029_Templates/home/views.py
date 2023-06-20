from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

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
    students =Student.objects.all()
    context={
        'students':students
    }
    return render(request, 'home/student_detail.html',context)



#---------form----------
from .forms import StudentForm
from django.shortcuts import redirect

def student_add(request):
    form=StudentForm()


    if request.method == 'POST' : 
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')


    context= {
        'form':form
    }
    return render(request,'home/student_add.html',context)


from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy

class StudentAddView(CreateView):
    model= Student
    form_class= StudentForm
    success_url= reverse_lazy('list')
    # defaults to 'home/student_form.html'
    template_name = 'home/student_add.html'


class StudentListView(ListView):
    model=Student
    template_name='home/student_list.html'
    #paginate_by= 5


class StudentDetailView(DetailView):
    model = Student
    # pk_url_kwarg = 'id'
    template_name = 'home/student_detail_2.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    # pk_url_kwarg = 'id'
    context_object_name = 'student'
    success_url = reverse_lazy('list')    


class StudentDeleteView(DeleteView):
    model = Student
    # pk_url_kwarg = 'id'
    success_url = reverse_lazy('list')
