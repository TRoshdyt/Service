from rest_framework import serializers
from .models import Tblguestinfo, Tblhotel, Tblnationality

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

