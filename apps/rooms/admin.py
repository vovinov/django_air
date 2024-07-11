from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomCustomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic info",
            {
                "fields": (
                    "title",
                    "description",
                    "country",
                    "address",
                    "price",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More about space",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                )
            },
        ),
        ("Last detail", {"fields": ("host",)}),
    )

    list_display = (
        "title",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
