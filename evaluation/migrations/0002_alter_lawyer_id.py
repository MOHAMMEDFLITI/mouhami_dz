# Generated by Django 4.2.8 on 2024-01-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lawyer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
