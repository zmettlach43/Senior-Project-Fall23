# Generated by Django 4.2.6 on 2023-11-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "SeniorProjectApp",
            "0011_customer_order_menuitem_image_delete_cart_order_item",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="description",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="carausel",
            name="image",
            field=models.ImageField(upload_to="uploads/carausel/"),
        ),
    ]
