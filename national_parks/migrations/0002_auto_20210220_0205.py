# Generated by Django 3.0.7 on 2021-02-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("national_parks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nationalparks",
            name="world_heritage_site",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
