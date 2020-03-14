# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CrimeReport(models.Model):
    acknowledgement_no = models.CharField(db_column='Acknowledgement_No',primary_key=True,max_length=264)  # Field name made lowercase. This field type is a guess.
    district = models.CharField(db_column='District', blank=True, null=True,max_length=264)  # Field name made lowercase.
    police_station = models.CharField(db_column='Police_Station', blank=True, null=True,max_length=264)  # Field name made lowercase.
    category = models.CharField(db_column='Category', blank=True, null=True,max_length=264)  # Field name made lowercase.
    sub_category = models.CharField(db_column='Sub_Category', blank=True, null=True,max_length=264)  # Field name made lowercase.
    status = models.CharField(db_column='Status', blank=True, null=True,max_length=264)  # Field name made lowercase.
    incident_date = models.DateField()  # Field name made lowercase.
    incident_place = models.CharField("Incident Location",blank=True, null=True,max_length=264)
    complaint_date = models.DateField()  # Field name made lowercase.   
    suspect_name = models.CharField("Suspect Name",blank=True, null=True,max_length=264)
    suspect_number = models.CharField("Suspect Number",blank=True, null=True,max_length=264)
    suspect_email = models.CharField("Suspect Email",blank=True, null=True,max_length=264)
    suspect_details = models.CharField("Other Suspect Details",blank=True, null=True,max_length=264)
    last_action_taken_on = models.DateField()  # Field name made lowercase.
    remarks = models.TextField("Remarks",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'CrimeReport'

    def __str__(self):
        return self.acknowledgement_no
