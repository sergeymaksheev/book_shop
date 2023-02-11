# Generated by Django 4.1.5 on 2023-02-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_book_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Orders",
            new_name="Order",
        ),
        migrations.RenameModel(
            old_name="Orders_detail",
            new_name="Order_detail",
        ),
        migrations.AddField(
            model_name="book",
            name="weight",
            field=models.IntegerField(
                help_text="Enter a book's weight here", null=True
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="year",
            field=models.CharField(
                help_text="Enter a year here", max_length=50, null=True
            ),
        ),
    ]
