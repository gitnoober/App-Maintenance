from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Apartment(models.Model):
    name = models.CharField(max_length=255)
    # flat = models.ForeignKey(Flat, on_delete=models.SET_NULL,null=True, blank=True)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Flat(models.Model):
    name = models.CharField(max_length=255)
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, null=True
    )
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.apartment}-{self.name}"


class CommitteeMember(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    contact_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )
    emergency_contact_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True
    )
    apartment_name = models.CharField(max_length=255, blank=True, null=True)
    flat_number = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=50, null=True)
    family_members = models.IntegerField(default=1)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.flat_number}"

    def get_absolute_url(self):
        return reverse("home")
