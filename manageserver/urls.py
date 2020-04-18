from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


app_name = 'manageserver'
urlpatterns = [
    path('', views.manager, name="manager"),
    path('editcfg/<int:id_server>', views.edit_cfg, name="editcfg"),
    path('editcarlist/<int:id_server>', views.edit_car_list, name="editcarlist"),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='manageserver/login.html',
            authentication_form=LoginForm
        ),
        name="login"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='acserver/index.html'),
        name="logout"
    ),
    path('upload/', views.upload, name="upload"),
]