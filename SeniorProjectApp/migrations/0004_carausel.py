# Generated by Django 4.2.6 on 2023-10-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SeniorProjectApp", "0003_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carausel",
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
                ("image", models.ImageField(upload_to="pics/%y/%m/%d/")),
                ("title", models.CharField(max_length=150)),
                ("sub_title", models.CharField(max_length=100)),
            ],
        ),
    ]
