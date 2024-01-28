from django.shortcuts import render
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, views
from rest_framework.response import Response
from django.http import QueryDict
import random

from .serializers import GuestInfoDetailedSerializer, GuestInfoSerializer, HotelSerializer, NationalitySerializer
from .models import Tblguestinfo, Tblhotel, Tblnationality
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
            registration_data = request.data.copy()
            sql_query = f"""
                DECLARE @SpecificID INT = (SELECT MAX(SpecificID) FROM tblSalesCompany_Holding) + 1;
                EXEC tblSalesCompany_Holding_UI
            """
            return Response(data=registration_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'result': e}, status=status.HTTP_400_BAD_REQUEST)
