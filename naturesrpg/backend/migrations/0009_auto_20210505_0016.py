# Generated by Django 3.2 on 2021-05-05 00:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20210505_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='strength',
            new_name='attack',
        ),
        migrations.AddField(
            model_name='player',
            name='team_mems',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='observation',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='num_of_obs',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
