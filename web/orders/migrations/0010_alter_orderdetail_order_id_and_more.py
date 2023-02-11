# Generated by Django 4.1.5 on 2023-02-08 13:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0009_alter_orderdetail_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetail",
            name="order_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.order"
            ),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="quantity",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="total_price",
            field=models.IntegerField(
                default=100, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
