# Generated by Django 4.0.4 on 2022-05-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_date_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
