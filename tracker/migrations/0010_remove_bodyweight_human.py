# Generated by Django 3.2.4 on 2021-06-25 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_bodyweight_human'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodyweight',
            name='human',
        ),
    ]
