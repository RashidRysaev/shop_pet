# Generated by Django 2.2.18 on 2021-03-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ordersapp", "0001_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="is_active",
            field=models.BooleanField(db_index=True, default=True, verbose_name="активен"),
        ),
    ]