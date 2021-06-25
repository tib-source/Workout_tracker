# Generated by Django 3.2.4 on 2021-06-25 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_weight'),
        ('tracker', '0008_routine_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodyweight',
            name='human',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
            preserve_default=False,
        ),
    ]