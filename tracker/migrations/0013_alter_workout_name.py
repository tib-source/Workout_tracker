# Generated by Django 3.2.4 on 2021-06-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20210625_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
