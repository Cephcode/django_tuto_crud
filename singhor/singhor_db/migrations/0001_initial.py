# Generated by Django 4.2 on 2023-05-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="singhor",
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
                ("autheur", models.CharField(max_length=250)),
                ("photo_auteur", models.ImageField(blank=True, upload_to="img")),
                ("age_autheur", models.IntegerField(default=0, null=True)),
                ("singhor", models.CharField(max_length=200)),
            ],
        ),
    ]
