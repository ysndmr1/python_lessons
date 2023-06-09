from django.db import models

# https://docs.djangoproject.com/en/4.2/topics/db/models/
class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default='none@cw.com',null=True, blank=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    picture=models.ImageField(upload_to='images/',default='',null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # Kayıt yapıldığı anki zamanı otomatik yaz.
    updated = models.DateTimeField(auto_now=True) # Kayıt güncellendiği anki zamanı otomatik yaz.

    def __str__(self): # Kayıt yazdır.
        return f'{self.first_name} {self.last_name} # {self.number}'
    
    class Meta: # Default özellikleri değiştir.
        # https://docs.djangoproject.com/en/4.2/ref/models/options/
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        ordering = ["-first_name"] # Ters sıralam için (DESC) sutun isminin başına - konur.

#------------------ Django Shelll------------

AGES = (
    (10, 'Age:10'),
    (20, 'Age:20'),
    (30, 'Age:30'),
    (40, 'Age:40'),
    (50, 'Age:50'),
    (60, 'Age:60'),
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, blank=True, null=True,choices=AGES)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age}'