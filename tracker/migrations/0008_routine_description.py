# Generated by Django 3.2.4 on 2021-06-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20210625_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
