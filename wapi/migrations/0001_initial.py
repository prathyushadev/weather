# Generated by Django 4.1.5 on 2023-02-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherAgg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_max_temp', models.CharField(max_length=255)),
                ('avg_min_temp', models.CharField(max_length=255)),
                ('total', models.CharField(max_length=255)),
                ('station', models.CharField(max_length=255, verbose_name='Station of Weather')),
                ('year', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateTimeField()),
                ('min_temp', models.CharField(blank=True, max_length=255, null=True, verbose_name='maximum temperature for that day')),
                ('max_temp', models.CharField(blank=True, max_length=255, null=True, verbose_name='minimum temperature for that day')),
                ('amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Amount of Precipitation')),
                ('station', models.CharField(max_length=255, verbose_name='Station of Weather')),
            ],
            options={
                'unique_together': {('tdate', 'min_temp', 'max_temp', 'amount')},
            },
        ),
    ]
