# Generated by Django 2.0.7 on 2019-07-09 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='image_preview',
        ),
    ]
