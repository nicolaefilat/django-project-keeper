# Generated by Django 2.0.7 on 2019-07-09 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20190709_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_preview',
        ),
    ]