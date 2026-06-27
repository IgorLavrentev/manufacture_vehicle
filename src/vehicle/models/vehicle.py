from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    cost = models.FloatField()  # стоимость
    year = models.IntegerField()  # Год выпуска
    mileage = models.IntegerField()  # пробег

    enterprise = models.ForeignKey(to='Enterprise', related_name='vehicle', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'vehicle'