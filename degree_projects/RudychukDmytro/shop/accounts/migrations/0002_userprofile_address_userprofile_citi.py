# Generated by Django 4.2 on 2023-05-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="address",
            field=models.CharField(default="non", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="citi",
            field=models.CharField(default="null", max_length=30),
            preserve_default=False,
        ),
    ]
