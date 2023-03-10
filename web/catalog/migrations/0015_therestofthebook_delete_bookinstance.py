# Generated by Django 4.1.5 on 2023-02-05 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_remove_book_quantity_bookinstance"),
    ]

    operations = [
        migrations.CreateModel(
            name="TheRestOfTheBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(help_text="Number of books in the store"),
                ),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.book",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="BookInstance",
        ),
    ]
