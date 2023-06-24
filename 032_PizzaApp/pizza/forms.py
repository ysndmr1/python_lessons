from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = [
            'user',  # Otomatik kayıt edilecek
            'pizza',  # GET veriden gelecek
        ]
        # Mevcut field'ların özelliklerini değiştir:
        # https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        # https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#overriding-the-default-fields
        widgets = {
            'size': forms.RadioSelect,
        }
