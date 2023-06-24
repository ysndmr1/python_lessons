from django import forms

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    # extra_field = forms.CharField(max_length=128, required=False)

    class Meta(UserCreationForm.Meta):
        fields = (
            'email',
            'username',
            'password',
            'password2',
            'first_name',
            'last_name',
            # 'extra_field',
        )