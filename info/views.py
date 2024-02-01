from django.shortcuts import render
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, views
from rest_framework.response import Response
from django.http import QueryDict
import random
import json
from decimal import Decimal


from .serializers import (
    GuestInfoDetailedSerializer, GuestInfoSerializer, HotelSerializer, NationalitySerializer,
    CollectionSerializer, PaymentServiceSerializer, SalesCompanyHoldingSerializer,
)
from .models import Tblguestinfo, Tblhotel, Tblnationality, Tblcollection, Tblcurrency, TblpaymentsService, TblsalescompanyHolding
from .utils import create_id


@api_view(['GET'])
def list_hotels(request):
    if request.method == 'GET':
        hotels = Tblhotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_nationalities(request):
    if request.method == 'GET':
        nationality = Tblnationality.objects.all()
        serializer = NationalitySerializer(nationality, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_registration(request, request_id):
    if request.method == 'GET':
        registration = Tblguestinfo.objects.filter(guestinfoid=request_id).first()
        if not registration:
            return Response(data={'error': 'no data'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GuestInfoDetailedSerializer(registration)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_registration(request):
    if request.method == 'POST':        
        registration_data = request.data.copy()
        registration_data['guestinfoid'] = create_id()
        serializer = GuestInfoSerializer(data=registration_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_registration(request, request_id):
    if request.method == 'PUT':
        registration = Tblguestinfo.objects.filter(guestinfoid=request_id).first()
        if not registration:
            return Response(data={'error': 'no data'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = GuestInfoSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_service(request, hotel_id):
    if request.method == 'GET':
        hotel = Tblhotel.objects.filter(hotelid=hotel_id).first()
        if hotel:
            hotel_name = hotel.hotel
        else:
            hotel_name = 'no hotel'
        with connection.cursor() as cursor:
            sql_query = f"""
                SELECT
                    s.servesID, s.ServesName, p.PUT, s.PriceAdult,
                    s.PriceChild, s.PriceInf, s.Currency
                FROM tblServes s LEFT JOIN tblPUT p
                    ON s.servesID = p.ServiceID AND p.HotelName = '{hotel_name}'
            """
            cursor.execute(sql_query)
            results = cursor.fetchall()

        # Now 'results' contains the data retrieved from the database
        # You can process the data as needed
        request_data = [
            {
                'id': i[0],
                'name': i[1],
                'put': i[2],
                'p_adult': i[3],
                'p_child': i[4],
                'p_inf': i[5],
                'currency': i[6],
            } for i in results
        ]

        return Response(data=request_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_exchange(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            sql_query = """
                SELECT c.Abbreviation, x.Rate
                FROM tblCurrency c
                JOIN tblExchangeRatePeriod x ON c.Abbreviation = x.Currency
                    AND CONVERT(DATE, GETDATE()) BETWEEN x.ExchangeDateFrom AND x.ExchangeDateTo
            """
            cursor.execute(sql_query)
            results = cursor.fetchall()

        request_data = [
            {
                'currency': i[0],
                'rate': i[1],
            } for i in results
        ]

        return Response(data=request_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_service(request):
    if request.method == 'POST':        
        
        try:
            request_data = request.data
            last_record = TblsalescompanyHolding.objects.last()
            max_id = last_record.specificid + 1 if last_record else 1
            nationality = Tblnationality.objects.filter(nationality=request_data['country']).first()
            nationality_id = nationality.nationalityid if nationality else None
            sales_data = [
                {
                    'specificid': max_id,
                    'transportcode': 0,
                    'fileno': f'Gue-{request_data["bookingId"]}',
                    'agencyid': 1,
                    'sellerid': 1,
                    'servesdate': service['date'],
                    'serviceid': service['id'],
                    'voucherno': f'Gue {request_data["bookingId"]}',
                    'hotel': request_data['hotel']['hotel'],
                    'roomno': None,
                    'adult': service['adult'],
                    'child': service['child'],
                    'inf': service['inf'],
                    'commissionco': 0,
                    'nationalityid': nationality_id,
                    'priceadult': service['pAdult'],
                    'pricechild': service['pChild'],
                    'priceinf': service['pInf'],
                    'discountperc': 0,
                    'discountvalue': 0,
                    'currency': service['currency'],
                    'put': service['pickupTime'],
                    'totalsales': service['price'],
                    'commvalue': 0,
                    'salesarrdate': request_data['date'],
                    'refund': False,
                    'posted': False,
                    'type': 'sal',
                    'branchid': 1,
                } for service in request_data['services']
            ]
            total_paid_egp = Decimal(0)
            payment = request_data['payment']
            exchange_rate = { exchange['currency']: exchange['rate'] for exchange in request_data['exchange'] }

            for exchange in request_data['exchange']:
                rate = exchange['rate']
                print('rate', rate)
                exchange_currency = exchange['currency']
                print('exchange_currency', exchange_currency)
                paid_in_exchange = payment[exchange_currency]
                print('paid_in_exchange', paid_in_exchange)
                value = round(Decimal(rate) * Decimal(paid_in_exchange), 2)
                print('value', value)
                total_paid_egp += value

            for service in request_data['services']:
                service_amount = service['price']
                ex_rate = exchange_rate[service['currency']]
                price_in_egp = round(Decimal(service_amount) * Decimal(ex_rate), 2)

                if total_paid_egp >= price_in_egp:
                    service['amount'] = service_amount
                    total_paid_egp -= price_in_egp
                    service['status'] = 3
                else:
                    service['amount'] = round(Decimal(total_paid_egp) / Decimal(ex_rate), 2)
                    service['status'] = 2
            collection_data = [
                { 
                    'operationid': max_id, 
                    'servicedate': service['date'], 
                    'sourceapp': 'sal', 
                    'amount': service['amount'], 
                    'currency': service['currency'], 
                    'branchid': 1, 
                    'status': service['status'], 
                    'guestid': request_data['bookingId'],
                } for service in request_data['services']
            ]
            # sales_serializer = SalesCompanyHoldingSerializer(data=sales_data, many=True)
            # collection_serializer = CollectionSerializer(data=collection_data, many=True)
            # if sales_serializer.is_valid():
            #     # sales_serializer.save()
            #     pass
            # else:
            #     print(sales_serializer.errors)
            
            # if collection_serializer.is_valid():
            #     collection_data.save()
            # else:
            #     print(collection_serializer.errors)

            sql_query = f"""
                DECLARE @SpecificID INT = (SELECT MAX(SpecificID) FROM tblSalesCompany_Holding) + 1;
                EXEC tblSalesCompany_Holding_UI
            """
            return Response(data=collection_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'result': e}, status=status.HTTP_400_BAD_REQUEST)
