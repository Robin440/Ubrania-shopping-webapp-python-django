# Generated by Django 4.2.3 on 2023-10-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Admin', '0006_remove_product_product_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
