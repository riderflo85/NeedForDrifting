from django.db import models


class Piste(models.Model):
    name = models.CharField(max_length=200, unique=True)
    addon = models.BooleanField(default=True, null=False)

class Server(models.Model):
    name = models.CharField(max_length=45, unique=True)
    path_download = models.CharField(max_length=500)
    path_upload = models.CharField(max_length=500)
    cars = models.CharField(max_length=700)
    piste = models.ForeignKey(Piste, on_delete=models.CASCADE)

    def listing_cars(self):
        cars = []
        for car in self.cars.split(' '):
            cars.append(car.replace('_', ' '))
        return cars
