from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    #joined = models.DateTimeField()
    #image= models.ImageField()
    created=models.DateTimeField(auto_now_add=True) # kayit yapildigi anki zamani otomatik yaz
    #updated=models.DateTimeField(auto_now=True) #kayit guncellendigi anki zamani otomatik yaz 

    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.number}'
    
    class Meta: # Default özellikleri değiştir.
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        ordering = ["-first_name"] # Ters sıralam için (DESC) sutun isminin başına - konur.