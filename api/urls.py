from django.urls import path
from .views import check_login_user

app_name = 'api'
urlpatterns = [
    # Vérifier les informations d'authentification de l'utilisateur
    path('check_login', check_login_user, name="check_login"),
    # Récupérer la liste des serveurs AC présent sur le VPS
    # Action à réaliser sur le serveur AC (start/stop/statu)
]
