# Generated by Django 4.2 on 2023-04-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="available",
            field=models.BooleanField(default=True, verbose_name="Наявність"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Створено"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="Детальний опис"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(db_index=True, max_length=150, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Ціна"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.CharField(
                db_index=True, max_length=150, unique=True, verbose_name="Посилання"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="uploaded",
            field=models.DateTimeField(auto_now=True, verbose_name="Оновлено"),
        ),
    ]
