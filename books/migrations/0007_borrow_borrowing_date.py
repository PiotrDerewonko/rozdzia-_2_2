# Generated by Django 4.2.10 on 2024-02-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_remove_borrow_borrowing_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrow",
            name="borrowing_date",
            field=models.DateTimeField(default="2024-02-29"),
        ),
    ]
