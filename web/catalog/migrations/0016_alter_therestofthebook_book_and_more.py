# Generated by Django 4.1.5 on 2023-02-05 15:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0015_therestofthebook_delete_bookinstance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="therestofthebook",
            name="book",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.book",
            ),
        ),
        migrations.AlterField(
            model_name="therestofthebook",
            name="quantity",
            field=models.IntegerField(
                default=0,
                help_text="Number of books in the store",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
