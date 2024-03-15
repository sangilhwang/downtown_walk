# Generated by Django 5.0.3 on 2024-03-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmpData",
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
                ("borough", models.CharField(max_length=20)),
                ("mtolfirstfloor", models.FloatField()),
                ("smallfirstfloor", models.FloatField()),
                ("empdensity", models.FloatField()),
                ("emptopopul", models.FloatField()),
            ],
        ),
    ]