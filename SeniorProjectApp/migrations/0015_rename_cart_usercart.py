# Generated by Django 4.2.7 on 2023-12-05 21:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SeniorProjectApp', '0014_cart_cartitem_cart_products_cart_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='UserCart',
        ),
    ]
