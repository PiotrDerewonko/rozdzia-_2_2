# Generated by Django 4.2.10 on 2024-02-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_borrow_borrowing_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrow",
            name="borrowing_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]