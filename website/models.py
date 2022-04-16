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


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name



class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
	
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)