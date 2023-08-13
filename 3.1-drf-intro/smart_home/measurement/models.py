from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)


class Measurement(models.Model):

    sens = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)