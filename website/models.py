# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator
# from django.db import models
# from django.urls import reverse

# Create your models here.


# class Apartment(models.Model):
#     name = models.CharField(max_length=255)
#     # flat = models.ForeignKey(Flat, on_delete=models.SET_NULL,null=True, blank=True)
#     added_on = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name}"


# class Flat(models.Model):
#     name = models.CharField(max_length=255)
#     apartment = models.ForeignKey(
#         Apartment, on_delete=models.CASCADE, null=True
#     )
#     added_on = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.apartment}-{self.name}"


# class CommitteeMember(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_regex = RegexValidator(
#         regex=r"^\+?1?\d{9,15}$",
#         message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
#     )
#     contact_number = models.CharField(
#         validators=[phone_regex], max_length=17, blank=True
#     )
#     emergency_contact_number = models.CharField(
#         validators=[phone_regex], max_length=17, blank=True, null=True
#     )
#     apartment_name = models.CharField(max_length=255, blank=True, null=True)
#     flat_number = models.CharField(max_length=50, blank=True, null=True)
#     blood_group = models.CharField(max_length=50, null=True)
#     family_members = models.IntegerField(default=1)
#     added_on = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name}-{self.flat_number}"

#     def get_absolute_url(self):
#         return reverse("home")


import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from indian_cities.dj_city import cities


class Apartment(models.Model):
    city = models.CharField(
        choices=cities, max_length=255, null=True, blank=True
    )
    apartment = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.apartment}"


class Building(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    building = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.building}"


class Flat(models.Model):
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, null=True
    )
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    flat = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.flat}"


class Role(models.Model):
    role = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.role)


class Facility(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    meta = models.CharField(max_length=255, null=True, blank=True)
    booked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "facility"
        verbose_name_plural = "facilities"

    def __str__(self):
        return f"{self.title}"


class Reservation(models.Model):
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reservation_ref = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )

    def __str__(self):
        return f"{self.facility} - {self.user}"
