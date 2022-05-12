# Generated by Django 4.0.4 on 2022-05-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_delete_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bar_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_id', models.IntegerField()),
                ('name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.TextField()),
            ],
        ),
    ]