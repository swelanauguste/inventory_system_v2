# Generated by Django 4.1.4 on 2022-12-15 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]