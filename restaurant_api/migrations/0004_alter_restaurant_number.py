# Generated by Django 4.1.4 on 2022-12-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0003_alter_restaurant_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]
