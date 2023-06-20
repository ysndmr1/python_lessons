from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profil_pic= models.ImageField(upload_to='profile_pics', blank=True)
    GENDER=[
        ('M','Male'),
        ('F','Famale'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"