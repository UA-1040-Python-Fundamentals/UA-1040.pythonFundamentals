# Generated by Django 4.2 on 2023-05-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_alter_order_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="weight_unit",
            field=models.TextField(default="kg", max_length=10),
        ),
    ]
