# Generated by Django 4.2 on 2023-05-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Notes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
