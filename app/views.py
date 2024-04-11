from venv import logger
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Hotels, Reservation, Guest
from app.serializers import HotelSerializers
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse("hello world!")

@api_view(["GET", "POST"])
def gethotels(request):
    if request.method == "GET":
        hotels = Hotels.objects.all()
        hotelSerializers = HotelSerializers(hotels, many = True)
        return Response(hotelSerializers.data)
    elif request.method == "POST":
        serializer = HotelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_hotel_by_id(request, id):
    if request.method == "GET":
        try:
            hotel = Hotels.objects.get(id=id)
            serializer = HotelSerializers(hotel)
            return Response(serializer.data)
        except Hotels.DoesNotExist:
            return Response({"message": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_reservation(request):
    if request.method == "POST":
        data = request.data
        logger.info("Received data: %s", data) #打印数据
        hotel_name = data.get('hotel_name')
        checkin_date = data.get('checkin')
        checkout_date = data.get('checkout')
        # 修正这里的键名
        guest_list = data.get('guests_list', [])  # 这里的键名应该是 guests_list

        try:
            hotel = Hotels.objects.get(name=hotel_name)
        except Hotels.DoesNotExist:
            return Response({"message": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
        
        reservation = Reservation.objects.create(hotel=hotel, checkin=checkin_date, checkout=checkout_date)

        for guest_info in guest_list:
            Guest.objects.create(reservation=reservation, **guest_info)

        # 设置 confirmation_number 为当前时间
        my_id = reservation.reservation_id
        # my_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        confirmation_number= my_id

        response_data = {
            "confirmation_number": confirmation_number
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
        
