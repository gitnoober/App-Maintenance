from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Apartment, Building, Facility, Flat, Reservation, Role


@admin.register(Apartment)
class ApartmentAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "apartment", "city"]


@admin.register(Building)
class BuildingAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "building"]


@admin.register(Flat)
class FlatAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "flat"]


@admin.register(Role)
class RoleAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "role"]


@admin.register(Facility)
class FacilityAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "apartment", "title", "booked"]


@admin.register(Reservation)
class ReservationAdmin(ImportExportActionModelAdmin):
    list_display = ["id", "facility", "start_time", "end_time"]
