# Generated by Django 4.2.4 on 2023-08-14 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("barbers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("notes", models.TextField(blank=True)),
                (
                    "preferred_barber",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="barbers.barber",
                    ),
                ),
            ],
        ),
    ]