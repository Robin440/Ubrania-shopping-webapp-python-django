# Generated by Django 4.2.3 on 2023-10-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Admin', '0011_product_prod_pic_three_product_prod_pic_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='section',
            name='section_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
