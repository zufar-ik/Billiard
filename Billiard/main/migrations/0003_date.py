# Generated by Django 4.0.4 on 2022-05-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nachalo', models.TimeField(verbose_name='%H:%M')),
                ('okonchanie', models.TimeField(verbose_name='%H:%M')),
            ],
        ),
    ]
