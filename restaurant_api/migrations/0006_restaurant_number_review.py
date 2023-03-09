# Generated by Django 4.1.4 on 2023-03-02 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0005_remove_restaurant_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='number',
            field=models.CharField(default=5552224445, max_length=12),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('restaurant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant_api.restaurant')),
            ],
        ),
    ]
