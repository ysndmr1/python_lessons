from django import forms 
from .models import Student


# class StudentForm(forms.Form):
#     first_name=forms.CharField(max_length=30)
#     last_name=forms.CharField(max_length=30)
#     number=forms.IntegerField()


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'first_name':'First Name',
        }