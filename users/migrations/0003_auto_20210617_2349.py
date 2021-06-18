# Generated by Django 3.2.4 on 2021-06-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210617_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
