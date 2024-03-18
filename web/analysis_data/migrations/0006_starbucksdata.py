# Generated by Django 5.0.3 on 2024-03-17 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis_data", "0005_rename_districtage_districtagedata"),
    ]

    operations = [
        migrations.CreateModel(
            name="StarbucksData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store_count", models.IntegerField()),
                ("store_ratio", models.FloatField()),
                (
                    "district_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analysis_data.districtdata",
                    ),
                ),
            ],
        ),
    ]
