# Generated by Django 3.1.4 on 2021-01-05 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='profile_name',
        ),
    ]