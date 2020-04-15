from django.urls import path
from . import views


app_name = 'acserver'
urlpatterns = [
    path('', views.index, name="index"),
    path('download/<int:id_server>', views.download, name="download"),
]
