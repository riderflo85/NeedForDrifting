from django.contrib.auth.forms import AuthenticationForm
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from acserver.listing_server import list_all_servers, list_all_cars, list_all_tracks


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

class UpdateCarForm(forms.Form):
    """ Add car in the database """

    name_car = forms.CharField(
        label='car',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )
    name_folder = forms.ChoiceField(
        label='foldername',
        choices=lazy(list_all_cars, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )
    is_car_addon = forms.BooleanField(
        label='iscaraddon',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'custom-control-input'}
        )
    )
    form_identifiant = forms.CharField(
        initial='car',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

class UpdateTrackForm(forms.Form):
    """ Add track in the database """

    name_track = forms.CharField(
        label='track',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )
    name_folder = forms.ChoiceField(
        label='foldername',
        choices=lazy(list_all_tracks, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )
    is_track_addon = forms.BooleanField(
        label='istrackaddon',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'custom-control-input'}
        )
    )
    form_identifiant = forms.CharField(
        initial='track',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )