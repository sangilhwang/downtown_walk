# Generated by Django 5.0.3 on 2024-03-15 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis_data", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeoulPopData",
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
                ("s10", models.IntegerField()),
                ("s20", models.IntegerField()),
                ("s30", models.IntegerField()),
                ("s40", models.IntegerField()),
                ("s50", models.IntegerField()),
                ("s60", models.IntegerField()),
                ("s70", models.IntegerField()),
                ("s80_s90", models.IntegerField()),
                ("total", models.IntegerField()),
                ("ratio_10s", models.FloatField()),
                ("ratio_20s", models.FloatField()),
                ("ratio_30s", models.FloatField()),
                ("ratio_40s", models.FloatField()),
                ("ratio_50s", models.FloatField()),
                ("ratio_60s", models.FloatField()),
                ("ratio_70s", models.FloatField()),
                ("ratio_80s_to_90s", models.FloatField()),
                ("ratio_total", models.FloatField()),
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
