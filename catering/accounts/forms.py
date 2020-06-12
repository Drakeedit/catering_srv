from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Чому ти тут використав класи, а у в'юхах - ф-ції??? Все через сраку! І де форма для Логіна. Тут тільки реєстрація....
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
