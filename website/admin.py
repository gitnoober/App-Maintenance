# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import CommitteeMember


# admin.site.register(Flat)
# admin.site.register(Apartment)
# admin.site.register(CommitteeMember)
class CommitteeMemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(CommitteeMember, CommitteeMemberAdmin)
