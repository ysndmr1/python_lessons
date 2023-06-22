# eger form yapisi uzerinde bir email eklemek istersek bu sekilde eoverride yapabiliriz
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# class CustomUserCreationForm(UserCreationForm):

#     extra_field = forms.CharField(max_length=128, required=False)

#     class Meta(UserCreationForm.Meta):
#         fields = (
#             'email',
#             'username',
#             'password',
#             'password2',
#             'first_name',
#             'last_name',
#             'extra_field',
#         )