# Generated by Django 5.0.4 on 2024-05-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mande", "0003_remove_monitorprojectmodel_overall_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectmodel",
            name="kochi",
            field=models.BooleanField(default=False, verbose_name="Kochi"),
        ),
    ]
