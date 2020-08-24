from django.urls import path
from .views import check_login_user, get_all_servers, run_cmd

app_name = 'api'
urlpatterns = [
    # Vérifier les informations d'authentification de l'utilisateur
    path('check_login', check_login_user, name="check_login"),
    # Récupérer la liste des serveurs AC présent sur le VPS
    path('get_servers', get_all_servers, name="get_servers"),
    # Action à réaliser sur le serveur AC (start/stop/statu)
    path('run_command', run_cmd, name="run_command"),
]
