# Generated by Django 5.1.7 on 2025-04-01 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_matatu_maintenance_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='core.user'),
        ),
        migrations.AlterField(
            model_name='tout',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tout', to='core.user'),
        ),
    ]
