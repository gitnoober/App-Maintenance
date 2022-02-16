# Generated by Django 4.0.1 on 2022-02-16 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_remove_apartment_flat_flat_apartment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="committeemember",
            name="flat_number",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.flat",
            ),
        ),
    ]
