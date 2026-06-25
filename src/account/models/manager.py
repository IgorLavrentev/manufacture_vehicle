from account.models.user import User
from django.db import models
from vehicle.models import Enterprise

class Manager(User):
    enterprises = models.ManyToManyField(
        to=Enterprise,
        related_name="managers",
    )

    objects = User.objects


    class Meta:
        db_table = "managers"
        verbose_name = "manager"
        verbose_name_plural = "managers"
