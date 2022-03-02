from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone

from website.models import Apartment, Building, Flat, Role

DEFAULT_ROLE_ID = 2


class Profile(models.Model):
    FLAT_STATUS = (("Tenant", "Tenant"), ("Owner", "Owner"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    role = models.ForeignKey(
        Role,
        default=DEFAULT_ROLE_ID,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, null=True, blank=True
    )
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, null=True, blank=True
    )
    flat = models.ForeignKey(
        Flat, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(
        choices=FLAT_STATUS, max_length=15, null=True, blank=True
    )
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
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
    blood_group = models.CharField(max_length=50, null=True)
    family_members = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("home")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
