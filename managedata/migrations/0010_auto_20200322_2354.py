# Generated by Django 3.0.4 on 2020-03-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0009_auto_20200316_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimereport',
            name='complaint_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='incident_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
