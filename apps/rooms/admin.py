from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomCustomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
