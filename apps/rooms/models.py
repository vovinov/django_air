from django.db import models

from django_countries.fields import CountryField

from common import models as common_models
from users import models as user_models


class AbstractItem(common_models.TimeStampModel):
    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class RoomType(AbstractItem):
    pass


class Room(common_models.TimeStampModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140, blank=True)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.title
