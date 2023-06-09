# Generated by Django 4.2.1 on 2023-06-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0005_rename_cover_worker_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("full_list", "all tasks"),
                    ("in_progress", "tasks that are being worked on"),
                    ("approved", "completed tasks"),
                ],
                max_length=63,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d"),
        ),
    ]
