# Generated by Django 4.0.4 on 2022-05-07 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_date_id_alter_date_stol_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='stol_id',
        ),
    ]
