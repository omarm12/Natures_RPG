# Generated by Django 3.2 on 2021-05-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20210505_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='taxon_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='observation',
            name='quality',
            field=models.CharField(default='needs_id', max_length=20),
        ),
    ]
