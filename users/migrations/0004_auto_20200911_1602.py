# Generated by Django 3.1.1 on 2020-09-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200911_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmed',
            new_name='eamil_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
