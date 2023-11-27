# Generated by Django 4.2.3 on 2023-11-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_blocked',
            field=models.BooleanField(default=False, help_text='Indicates whether the user is blocked.'),
        ),
    ]