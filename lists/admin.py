from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAmdin(admin.ModelAdmin):
    pass