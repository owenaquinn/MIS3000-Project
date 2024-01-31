# Generated by Django 5.0.1 on 2024-01-30 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_alter_times_end_alter_times_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeringtimes',
            name='offeringDayID',
        ),
        migrations.DeleteModel(
            name='Times',
        ),
        migrations.AddField(
            model_name='offeringdays',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='src.days'),
        ),
        migrations.AddField(
            model_name='offeringdays',
            name='endTime',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='offeringdays',
            name='startTime',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='OfferingTimes',
        ),
    ]
