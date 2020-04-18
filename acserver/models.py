from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=200, unique=True)
    addon = models.BooleanField(default=True, null=False)


class Car(models.Model):
    name = models.CharField(max_length=200, unique=True)
    addon = models.BooleanField(default=True, null=False)


class Server(models.Model):
    name = models.CharField(max_length=45, unique=True)
    path_download = models.CharField(max_length=500)
    path_upload = models.CharField(max_length=500)
    file_cfg = models.CharField(max_length=500)
    file_entry_list = models.CharField(max_length=500)
    cars = models.ManyToManyField(Car)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
