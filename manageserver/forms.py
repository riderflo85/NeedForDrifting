from django.contrib.auth.forms import AuthenticationForm
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from acserver.listing_server import list_all_servers


def validate_zip_file(value):
    accept = ['cars.zip', 'track.zip']
    if str(value) not in accept:
        raise ValidationError(
            _("%(value)s n'est pas acceptée"),
            params={"value": value},
        )

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

class UploadFileForm(forms.Form):
    """ Upload file form """

    all_servers = forms.ChoiceField(
        label='servers',
        choices=lazy(list_all_servers, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    file = forms.FileField(
        validators=[validate_zip_file],
        label='file',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file',
                'accept': '.zip,application/zip',
            },
        )
    )