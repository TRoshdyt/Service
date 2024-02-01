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



class TblsalescompanyHolding(models.Model):
    salescompanyid = models.AutoField(db_column='SalesCompanyID', primary_key=True)  # Field name made lowercase.
    specificid = models.IntegerField(db_column='SpecificID', blank=True, null=True)  # Field name made lowercase.
    transportcode = models.CharField(db_column='TransportCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fileno = models.CharField(db_column='FileNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agencyid = models.SmallIntegerField(db_column='AgencyID', blank=True, null=True)  # Field name made lowercase.
    sellerid = models.IntegerField(db_column='SellerID', blank=True, null=True)  # Field name made lowercase.
    servesdate = models.DateField(db_column='ServesDate', blank=True, null=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hotel = models.CharField(db_column='Hotel', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    area = models.SmallIntegerField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    roomno = models.CharField(db_column='RoomNo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adult = models.IntegerField(db_column='Adult', blank=True, null=True)  # Field name made lowercase.
    child = models.IntegerField(db_column='Child', blank=True, null=True)  # Field name made lowercase.
    inf = models.IntegerField(db_column='Inf', blank=True, null=True)  # Field name made lowercase.
    commissionco = models.DecimalField(db_column='CommissionCo', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    invoice = models.BooleanField(db_column='Invoice', blank=True, null=True)  # Field name made lowercase.
    nationalityid = models.IntegerField(db_column='NationalityID', blank=True, null=True)  # Field name made lowercase.
    priceadult = models.DecimalField(db_column='PriceAdult', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricechild = models.DecimalField(db_column='PriceChild', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    priceinf = models.DecimalField(db_column='PriceInf', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountperc = models.DecimalField(db_column='DiscountPerc', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discountvalue = models.DecimalField(db_column='DiscountValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currency = models.ForeignKey('Tblcurrency', models.DO_NOTHING, db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    put = models.CharField(db_column='PUT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    totalsales = models.DecimalField(db_column='TotalSales', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    commvalue = models.DecimalField(db_column='CommValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesarrdate = models.DateField(db_column='SalesArrDate', blank=True, null=True)  # Field name made lowercase.
    mcrid = models.IntegerField(db_column='MCrID', blank=True, null=True)  # Field name made lowercase.
    paidpolicy = models.CharField(db_column='PaidPolicy', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typeofpaid = models.CharField(db_column='TypeOfPaid', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    brokerascustid = models.CharField(db_column='BrokerAsCustID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    brokerassuppid = models.CharField(db_column='BrokerAsSuppID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    boatid = models.IntegerField(db_column='BoatID', blank=True, null=True)  # Field name made lowercase.
    ourrep = models.CharField(db_column='OurRep', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    repid = models.IntegerField(db_column='RepID', blank=True, null=True)  # Field name made lowercase.
    leaderid = models.IntegerField(db_column='LeaderID', blank=True, null=True)  # Field name made lowercase.
    addedboat = models.BooleanField(db_column='AddedBoat', blank=True, null=True)  # Field name made lowercase.
    addedsupplier = models.BooleanField(db_column='AddedSupplier', blank=True, null=True)  # Field name made lowercase.
    totransportation = models.BooleanField(db_column='ToTransportation', blank=True, null=True)  # Field name made lowercase.
    refund = models.BooleanField(db_column='Refund', blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grouping = models.CharField(db_column='Grouping', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    posteduserid = models.SmallIntegerField(db_column='PostedUserID', blank=True, null=True)  # Field name made lowercase.
    posteddate = models.DateTimeField(db_column='PostedDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.SmallIntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    userdate = models.DateTimeField(db_column='UserDate', blank=True, null=True)  # Field name made lowercase.
    modifyid = models.SmallIntegerField(db_column='ModifyID', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    transpolicy = models.CharField(db_column='TransPolicy', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    collectionstatus = models.IntegerField(db_column='CollectionStatus', blank=True, null=True)  # Field name made lowercase.
    jvnu = models.IntegerField(db_column='JVNu', blank=True, null=True)  # Field name made lowercase.
    starttrip = models.CharField(db_column='StartTrip', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    endtrip = models.CharField(db_column='EndTrip', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSalesCompany_Holding'


class Tblcollection(models.Model):
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  # Field name made lowercase.
    operationid = models.IntegerField(db_column='OperationID', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.DateField(db_column='ServiceDate', blank=True, null=True)  # Field name made lowercase.
    sourceapp = models.CharField(db_column='SourceApp', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iscustomer = models.BooleanField(db_column='IsCustomer', blank=True, null=True)  # Field name made lowercase.
    repname = models.CharField(db_column='RepName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    treasuryid = models.IntegerField(db_column='TreasuryID', blank=True, null=True)  # Field name made lowercase.
    receipt = models.CharField(db_column='Receipt', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    signatureid = models.IntegerField(db_column='SignatureID', blank=True, null=True)  # Field name made lowercase.
    treasurydate = models.DateField(db_column='TreasuryDate', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    userdate = models.DateTimeField(db_column='UserDate', blank=True, null=True)  # Field name made lowercase.
    modifyid = models.IntegerField(db_column='ModifyID', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    guestid = models.IntegerField(db_column='GuestID', blank=True, null=True)  # Field name made lowercase.
    depinformed = models.CharField(db_column='DepInformed', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCollection'


class TblpaymentsService(models.Model):
    payment_id = models.AutoField(primary_key=True)
    operation_id = models.IntegerField(db_column='Operation_id')  # Field name made lowercase.
    jvnu = models.IntegerField(db_column='JVNu')  # Field name made lowercase.
    invoice_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_currency = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    payment_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    basic_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_receipt = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    payment_treasuryid = models.IntegerField(db_column='payment_treasuryID', blank=True, null=True)  # Field name made lowercase.
    repname = models.CharField(db_column='RepName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    definecode = models.CharField(db_column='DefineCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    signatureid = models.IntegerField(db_column='SignatureID', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    userid = models.SmallIntegerField(blank=True, null=True)
    user_date = models.DateField(blank=True, null=True)
    modify_id = models.SmallIntegerField(blank=True, null=True)
    modify_date = models.DateField(blank=True, null=True)
    payment_localc = models.DecimalField(db_column='payment_localC', max_digits=21, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPayments_Service'


class Tblcurrency(models.Model):
    currencyid = models.IntegerField(db_column='CurrencyID',)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', primary_key=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    kindofcurrency = models.CharField(db_column='KindOfCurrency', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subunit = models.CharField(db_column='subUnit', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chartaccount = models.CharField(db_column='ChartAccount', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid = models.SmallIntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCurrency'