# Generated by Django 3.1 on 2020-09-03 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200901_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amenity',
            new_name='amenities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='bedroomes',
            new_name='bedrooms',
        ),
    ]
