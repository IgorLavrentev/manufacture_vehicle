from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)



    def __str__(self):
        return self.name


    class Meta:
        db_table = 'enterprise'