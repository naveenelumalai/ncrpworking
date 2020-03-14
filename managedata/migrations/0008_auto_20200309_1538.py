# Generated by Django 3.0.4 on 2020-03-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0007_auto_20200309_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimereport',
            name='incident_place',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Incident Location'),
        ),
        migrations.AddField(
            model_name='crimereport',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Remarks'),
        ),
        migrations.AddField(
            model_name='crimereport',
            name='suspect_details',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Other Suspect Details'),
        ),
        migrations.AddField(
            model_name='crimereport',
            name='suspect_email',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Suspect Email'),
        ),
        migrations.AddField(
            model_name='crimereport',
            name='suspect_name',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Suspect Name'),
        ),
        migrations.AddField(
            model_name='crimereport',
            name='suspect_number',
            field=models.CharField(blank=True, max_length=264, null=True, verbose_name='Suspect Number'),
        ),
    ]
