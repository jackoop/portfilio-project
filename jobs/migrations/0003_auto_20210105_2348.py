# Generated by Django 2.0.2 on 2021-01-05 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210105_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]