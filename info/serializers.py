from rest_framework import serializers
from .models import (
    Tblguestinfo, Tblhotel, Tblnationality, Tblcollection, TblsalescompanyHolding,
    TblpaymentsService, Tblcurrency
)


class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblhotel
        fields = ('hotelid', 'hotel', )


class NationalitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblnationality
        fields = ('nationalityid', 'nationality', )


class GuestInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblguestinfo
        fields = ('guestinfoid', 'arrivaldate', 'departuredate', 'guestname', 'viawhatsapp',
                  'genderfemale', 'mailaddress', 'cityresidence', 'country', 'whatsappphone',
                  'phoneegypt', 'dateofbirth', 'hotelname', 'adult', 'child', 'inf', )


class GuestInfoDetailedSerializer(serializers.ModelSerializer):
    hotel_data = serializers.SerializerMethodField()
    
    def get_hotel_data(self, obj):
        hotel = Tblhotel.objects.filter(hotelid=obj.hotelname).first()
        if hotel:
            return {
                'hotel_id': hotel.hotelid,
                'hotel': hotel.hotel
            }
        return {'hotel_id': 0, 'hotel': ''}
    
    class Meta:
        model = Tblguestinfo
        fields = ('guestinfoid', 'arrivaldate', 'departuredate', 'guestname', 'viawhatsapp',
                  'genderfemale', 'mailaddress', 'cityresidence', 'country', 'whatsappphone',
                  'phoneegypt', 'dateofbirth', 'hotel_data', 'adult', 'child', 'inf', )


class SalesCompanyHoldingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblsalescompanyHolding
        fields = (
            'salescompanyid', 'specificid', 'transportcode', 'fileno', 'agencyid', 'sellerid', 'servesdate',
            'serviceid', 'voucherno', 'hotel', 'roomno', 'adult', 'child', 'inf', 'commissionco', 'nationalityid', 'priceadult',
            'pricechild', 'priceinf', 'discountperc', 'discountvalue', 'currency', 'put', 'totalsales',
            'commvalue', 'salesarrdate', 'refund', 'posted', 'type', 'branchid',
        )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tblcollection
        fields = (
            'collectionid', 'operationid', 'servicedate', 'sourceapp', 'amount',
            'currency', 'branchid', 'status', 'guestid',
        )


class PaymentServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblpaymentsService
        fields = (
            'payment_id', 'operation_id', 'invoice_number', 'payment_date', 'payment_amount',
            'payment_currency', 'payment_rate', 'basic_rate', 'definecode', 'source', 'due_date',
            'branchid', 'payment_localc', 
        )
