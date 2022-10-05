# Generated by Django 4.1.1 on 2022-10-05 14:34

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.TextField(unique=True),
        ),
    ]
