# Generated by Django 4.2.5 on 2023-11-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeniorProjectApp', '0013_alter_menuitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
