# Generated by Django 2.0.7 on 2019-07-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190709_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_preview',
            field=models.TextField(),
        ),
    ]