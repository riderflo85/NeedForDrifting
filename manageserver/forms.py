from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """ Login form """

    username = forms.CharField(
        label='user',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pseudo', 'class': 'form-control'}
            ),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
            ),
    )
