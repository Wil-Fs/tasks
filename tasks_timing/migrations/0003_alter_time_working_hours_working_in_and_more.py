# Generated by Django 5.1.2 on 2024-10-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks_timing", "0002_remove_time_working_hours_working_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="time_working",
            name="hours_working_in",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="time_working",
            name="hours_working_out",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
