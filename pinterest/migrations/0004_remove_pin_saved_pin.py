# Generated by Django 4.0.1 on 2023-04-12 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest', '0003_savedpin_pin_saved_pin_savedpin_pin_savedpin_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin',
            name='saved_pin',
        ),
    ]
