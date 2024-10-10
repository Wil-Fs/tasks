# Generated by Django 5.1.2 on 2024-10-10 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks_timing", "0003_alter_time_working_hours_working_in_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeWorking",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("job_description", models.CharField(max_length=800)),
                (
                    "hours_working_in",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "hours_working_out",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "hours_worked",
                    models.DurationField(blank=True, editable=False, null=True),
                ),
                ("time_in", models.BooleanField(default=False)),
                ("time_out", models.BooleanField(default=False)),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks_timing.task",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Time_Working",
        ),
    ]
