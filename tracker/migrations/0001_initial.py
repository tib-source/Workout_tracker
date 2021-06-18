# Generated by Django 3.2.4 on 2021-06-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(choices=[('LW', 'Loosing Weight'), ('GM', 'Gaining Muscle')], default='Gaining Muscle', max_length=20)),
            ],
        ),
    ]
