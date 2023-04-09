# Generated by Django 4.0.1 on 2023-04-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_alter_userprofile_cover_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, default='', verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, default='', verbose_name='Website'),
        ),
    ]
