from django.db import models
from common.models import TimeStampModel


class List(TimeStampModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self) -> str:
        return self.name
