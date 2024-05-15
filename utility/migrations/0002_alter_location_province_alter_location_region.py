# Generated by Django 5.0.4 on 2024-05-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utility", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="province",
            field=models.CharField(max_length=150, verbose_name="Province"),
        ),
        migrations.AlterField(
            model_name="location",
            name="region",
            field=models.CharField(max_length=150, verbose_name="Region"),
        ),
    ]
