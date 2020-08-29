from django.urls import path
from .views import check_login_user, get_all_servers, get_all_tracks, run_cmd, change_track

app_name = 'api'
urlpatterns = [
    # Vérifier les informations d'authentification de l'utilisateur
    path('check_login', check_login_user, name="check_login"),
    # Récupérer la liste des serveurs AC présent sur le VPS
    path('get_servers', get_all_servers, name="get_servers"),
    # Récupérer la liste des pistes
    path('get_tracks', get_all_tracks, name="get_tracks"),
    # Action à réaliser sur le serveur AC (start/stop/statu)
    path('run_command', run_cmd, name="run_command"),
    # Changer de piste sur le serveur AC
    path('change_track', change_track, name="change_track"),
]
