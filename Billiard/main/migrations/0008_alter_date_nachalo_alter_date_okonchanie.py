# Generated by Django 4.0.4 on 2022-05-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_date_stol_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='nachalo',
            field=models.TimeField(verbose_name='%H%M'),
        ),
        migrations.AlterField(
            model_name='date',
            name='okonchanie',
            field=models.TimeField(null=True, verbose_name='%H%M'),
        ),
    ]