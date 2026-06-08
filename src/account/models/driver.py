from account.models.user import User
from django.db import models
from vehicle.models import Enterprise

class Driver(User):
    enterprise = models.ForeignKey(
        to=Enterprise,
        related_name="drivers",
        on_delete=models.CASCADE
    )
    class Meta:
        db_table = "drivers"
        verbose_name = "driver"
        verbose_name_plural = "drivers"