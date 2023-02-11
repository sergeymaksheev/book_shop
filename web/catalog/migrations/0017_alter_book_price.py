# Generated by Django 4.1.5 on 2023-02-07 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0016_alter_therestofthebook_book_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.IntegerField(
                help_text="Write your price here",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
