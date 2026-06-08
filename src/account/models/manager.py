from account.models.user import User
from django.db import models
from vehicle.models import Enterprise

class Manager(User):
    enterprise = models.ForeignKey(
        to=Enterprise,
        related_name="managers",
        on_delete=models.CASCADE
    )
    class Meta:
        db_table = "managers"
        verbose_name = "manager"
        verbose_name_plural = "managers"
