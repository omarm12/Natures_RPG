# Generated by Django 3.2 on 2021-05-07 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20210507_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='taxon_id',
        ),
    ]
