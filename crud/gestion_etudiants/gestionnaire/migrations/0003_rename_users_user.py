# Generated by Django 4.2 on 2023-04-16 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestionnaire", "0002_rename_user_users"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]
