# Generated by Django 4.1.5 on 2023-01-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "date_of_death",
                    models.DateField(blank=True, null=True, verbose_name="Died"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                    "name",
                    models.CharField(
                        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=150, verbose_name="Title")),
                (
                    "summary",
                    models.TextField(
                        help_text="Enter a brief description of the book",
                        max_length=1000,
                    ),
                ),
                ("isbn", models.CharField(max_length=13, verbose_name="ISBN")),
                ("author", models.ManyToManyField(to="catalog.author")),
                (
                    "genre",
                    models.ManyToManyField(
                        help_text="Select a genre for this book", to="catalog.genre"
                    ),
                ),
            ],
        ),
    ]
