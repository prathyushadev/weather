from django.db import models

# Create your models here.


class Weather(models.Model):
    tdate = models.DateTimeField()
    min_temp = models.CharField(max_length=255, verbose_name="maximum temperature for that day", null=True, blank=True)
    max_temp = models.CharField(max_length=255, verbose_name="minimum temperature for that day", null=True, blank=True)
    amount = models.CharField(max_length=255, verbose_name="Amount of Precipitation", null=True, blank=True)
    station = models.CharField(max_length=255, verbose_name="Station of Weather")

    def __str__(self):
        return f"{self.tdate} - {self.min_temp} - {self.max_temp} - {self.amount}"

    class Meta:
        unique_together = ('tdate', 'min_temp', 'max_temp', 'amount')


class WeatherAgg(models.Model):
    year = models.CharField(max_length=255)
    avg_max_temp = models.CharField(max_length=255)
    avg_min_temp = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    station = models.CharField(max_length=255, verbose_name="Station of Weather")

    def __str__(self):
        return f"{self.year} - {self.avg_max_temp} - {self.avg_min_temp}"
