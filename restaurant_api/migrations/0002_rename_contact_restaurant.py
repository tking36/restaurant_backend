# Generated by Django 4.1.4 on 2022-12-22 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Restaurant',
        ),
    ]
