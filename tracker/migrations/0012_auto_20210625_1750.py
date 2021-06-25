# Generated by Django 3.2.4 on 2021-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_remove_workout_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='user',
        ),
        migrations.AddField(
            model_name='workout',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='workout',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
