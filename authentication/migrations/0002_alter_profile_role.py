# Generated by Django 4.0.1 on 2022-03-02 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0014_building_facility_reservation_role_and_more"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.ForeignKey(
                blank=True,
                default=2,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.role",
            ),
        ),
    ]
