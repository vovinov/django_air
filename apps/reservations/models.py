from django.db import models
from common.models import TimeStampModel


class Reservation(TimeStampModel):
    STATUS_PENDING = "Pending"
    STATUS_CONFIRMED = "Comfirmed"
    STATUS_CANCELED = "Canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "PENDING"),
        (STATUS_CONFIRMED, "CONFIRMED"),
        (STATUS_CANCELED, "CANCELED"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} / {self.check_in} - {self.check_out}"
