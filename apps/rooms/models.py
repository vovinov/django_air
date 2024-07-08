from django.db import models

from django_countries.fields import CountryField

from common import models as common_models


class AbstractItem(common_models.TimeStampModel):
    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class RoomType(AbstractItem):
    pass


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    pass


class Photo(common_models.TimeStampModel):
    caption = models.CharField(max_length=100)
    file = models.ImageField
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.title
