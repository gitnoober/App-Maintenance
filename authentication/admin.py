from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(ImportExportActionModelAdmin):
    date_hierarchy = "timestamp"
    list_display = ["id", "user", "role", "timestamp"]
    ordering = ("-timestamp",)
