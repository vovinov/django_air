from django.contrib import admin
from . import models


@admin.register(models.Reviews)
class ReviewAdminModel(admin.ModelAdmin):
    pass
