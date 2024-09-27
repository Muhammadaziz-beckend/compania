from django.contrib import admin
from .models import *


@admin.register(Catigori_woork)
class CatigoriAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Sotrudnic)
class SotrudnicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "jod")
    list_display_links = ("id", "name", "email", "jod")
    search_fields = ("name", "email", "jod")
    list_filter = ("jod",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_end")
    list_display_links = ("id", "name", "date_end")
    list_filter = ("date_end",)
