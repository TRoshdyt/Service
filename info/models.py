# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblguestinfo(models.Model):
    guestinfoid = models.IntegerField(db_column='GuestInfoID', primary_key=True)  # Field name made lowercase.
    filenumber = models.CharField(db_column='FileNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visitdate = models.DateField(db_column='VisitDate', blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='ArrivalDate', blank=True, null=True)  # Field name made lowercase.
    departuredate = models.DateField(db_column='DepartureDate', blank=True, null=True)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    viawhatsapp = models.BooleanField(db_column='ViaWhatsApp', blank=True, null=True)  # Field name made lowercase.
    genderfemale = models.BooleanField(db_column='GenderFemale', blank=True, null=True)  # Field name made lowercase.
    mailaddress = models.CharField(db_column='MailAddress', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cityresidence = models.CharField(db_column='CityResidence', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    whatsappphone = models.CharField(db_column='WhatsAppPhone', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phoneegypt = models.CharField(db_column='PhoneEgypt', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    hotelname = models.CharField(db_column='HotelName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    roomno = models.CharField(db_column='RoomNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    userdate = models.DateTimeField(db_column='UserDate', blank=True, null=True)  # Field name made lowercase.
    modifyid = models.IntegerField(db_column='ModifyID', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    adult = models.IntegerField(db_column='Adult', blank=True, null=True)  # Field name made lowercase.
    child = models.IntegerField(db_column='Child', blank=True, null=True)  # Field name made lowercase.
    inf = models.IntegerField(db_column='Inf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGuestInfo'


class Tblhotel(models.Model):
    hotelid = models.IntegerField(db_column='HotelID')  # Field name made lowercase.
    hotel = models.CharField(db_column='Hotel', primary_key=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    areaid = models.SmallIntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    indexposition = models.SmallIntegerField(db_column='IndexPosition', blank=True, null=True)  # Field name made lowercase.
    hotelimage1 = models.BinaryField(db_column='HotelImage1', blank=True, null=True)  # Field name made lowercase.
    hotelimage2 = models.BinaryField(db_column='HotelImage2', blank=True, null=True)  # Field name made lowercase.
    chartaccount = models.CharField(db_column='ChartAccount', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblHotel'


class Tblnationality(models.Model):
    nationalityid = models.SmallAutoField(db_column='NationalityID', primary_key=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNationality'
