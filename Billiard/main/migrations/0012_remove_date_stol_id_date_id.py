# Generated by Django 4.0.4 on 2022-05-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_date_id_alter_date_stol_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='stol_id',
        ),
        migrations.AddField(
            model_name='date',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
