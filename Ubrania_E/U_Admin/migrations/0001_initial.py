# Generated by Django 4.2.3 on 2023-11-25 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0002_customer_is_blocked'),
    ]

    operations = [
      
      
        migrations.CreateModel(
            name='Offer_Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_c_name', models.CharField(max_length=150)),
                ('discount', models.IntegerField(blank=True)),
                ('validity', models.DateField()),
            ],
        ),
    ]
      
      
     
      
  
     
    
