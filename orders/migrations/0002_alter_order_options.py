# Generated by Django 4.1.1 on 2022-10-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ("-created",),
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]
