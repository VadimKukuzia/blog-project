# Generated by Django 3.1.4 on 2021-01-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='New User', max_length=150),
        ),
    ]