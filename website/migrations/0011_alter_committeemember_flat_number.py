# Generated by Django 4.0.1 on 2022-02-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_alter_committeemember_flat_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="committeemember",
            name="flat_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
