# Generated by Django 4.2.3 on 2023-10-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Admin', '0009_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
