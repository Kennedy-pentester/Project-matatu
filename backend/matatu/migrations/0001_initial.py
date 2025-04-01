# Generated by Django 5.1.5 on 2025-03-29 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matatu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('driver', models.CharField(max_length=100)),
                ('conductor', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=14)),
                ('available_seats', models.IntegerField(default=14)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('date', models.DateField()),
                ('matatu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matatu.matatu')),
            ],
        ),
    ]
