from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=200, unique=True)
    folder_name = models.CharField(max_length=200)
    addon = models.BooleanField(default=True, null=False)


class Car(models.Model):
    name = models.CharField(max_length=200, unique=True)
    folder_name = models.CharField(max_length=200)
    addon = models.BooleanField(default=True, null=False)


class Server(models.Model):
    name = models.CharField(max_length=45, unique=True)
    path_download = models.CharField(max_length=500)
    path_upload = models.CharField(max_length=500)
    file_cfg = models.CharField(max_length=500)
    file_entry_list = models.CharField(max_length=500)
    cars = models.ManyToManyField(Car)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    status = models.CharField(max_length=11)
    name_cmd = models.CharField(max_length=16)