# Generated by Django 4.2.5 on 2023-11-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeniorProjectApp', '0013_menuitem_active_menuitem_description_menuitem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(),
        ),
    ]
