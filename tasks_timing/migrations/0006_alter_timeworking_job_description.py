# Generated by Django 5.1.2 on 2024-10-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks_timing", "0005_remove_timeworking_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeworking",
            name="job_description",
            field=models.CharField(default="Sem detalhes registrados!", max_length=800),
        ),
    ]
