from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Бренд')
    vehicle_type = models.CharField(max_length=20, verbose_name='Тип') # тип: passenger_car, truck, bus
    number_of_seats = models.PositiveIntegerField(verbose_name='Количество мест') # количество мест
    tank_capacity = models.PositiveIntegerField(verbose_name='Объем бака') # объем бака

    vehicle = models.ForeignKey(to = 'Vehicle', related_name='brands', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'brand'
