# Generated by Django 4.0.4 on 2022-05-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nachalo', models.TimeField()),
                ('okonchanie', models.TimeField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
