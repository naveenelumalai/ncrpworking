# Generated by Django 3.0.4 on 2020-03-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0002_auto_20200309_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimereport',
            name='acknowledgement_no',
            field=models.CharField(db_column='Acknowledgement_No', max_length=264, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='category',
            field=models.CharField(blank=True, db_column='Category', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='complaint_date',
            field=models.DateField(blank=True, db_column='Complaint_Date', null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='district',
            field=models.CharField(blank=True, db_column='District', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='incident_date',
            field=models.DateField(blank=True, db_column='Incident_Date', null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='last_action_taken_on',
            field=models.DateField(blank=True, db_column='Last_Action_Taken_on', null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='police_station',
            field=models.CharField(blank=True, db_column='Police_Station', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='status',
            field=models.CharField(blank=True, db_column='Status', max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='crimereport',
            name='sub_category',
            field=models.CharField(blank=True, db_column='Sub_Category', max_length=264, null=True),
        ),
    ]
