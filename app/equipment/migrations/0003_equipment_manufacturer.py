# Generated by Django 4.1.4 on 2022-12-15 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0002_manufacturer"),
    ]

    operations = [
        migrations.AddField(
            model_name="equipment",
            name="manufacturer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="manufacturer_list",
                to="equipment.manufacturer",
            ),
        ),
    ]
