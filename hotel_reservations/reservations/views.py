from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .models import *
from .serializers import HotelSerializer, ReservationsSerializer
from rest_framework.views import APIView
from rest_framework import status
from .swagger_decorators import *




# Create your views here.
def hotel_list(request):
    hotels = Hotel.objects.all()
    data = [{
        'id': hotel.pk,
        'description': hotel.description,
        'price': hotel.price,
        'created_at': hotel.create_at
    } for hotel in hotels]
    return JsonResponse({'hotels': data})


def detail_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    data = {
        'id': hotel.pk,
        'description': hotel.description,
        'price': hotel.price,
        'created_at': hotel.create_at
    }
    return JsonResponse({'hotels': data})


def del_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.delete()
    return HttpResponseRedirect('/hotel')


def res_list(request):
    reservations = Reservations.objects.all()
    data = [{
        'id': reservation.pk,
        'date_start': reservation.date_start,
        'date_end': reservation.date_end,
        'hotel': reservation.hotel
    } for reservation in reservations]
    return JsonResponse({'reservations': data})


def res_hotel_detail(request, pk):
    reservations = Reservations.objects.filter(hotel=pk)

    data = [{
        'id': reservation.id,
        'date_start': reservation.date_start,
        'date_end': reservation.date_end,
        'hotel': reservation.hotel
    } for reservation in reservations]
    return JsonResponse({'reservations_hotel': data})

def res_del(request, pk):
    res = Reservations.objects.get(pk=pk)
    res.delete()
    return HttpResponseRedirect('/reservation')


class HotelAPIView(APIView):
    @hotel_list_get_schema
    def get(self, request):
        hotels = Hotel.objects.all()

        sort_by = request.GET.get('sort_by', 'create_at')
        order = request.GET.get('order', 'desc')

        # Используем параметр sort_by из запроса
        if sort_by == 'price':
            sort_field = 'price'
        else:  # по умолчанию сортируем по create_at
            sort_field = 'create_at'

        # Применяем сортировку
        if order == 'asc':
            hotels = hotels.order_by(sort_field)
        else:
            hotels = hotels.order_by(f'-{sort_field}')
            
        data = [{
            'id': hotel.id,
            'description': hotel.description,
            'price': str(hotel.price), 
            'create_at': hotel.create_at.isoformat() if hotel.create_at else None
        } for hotel in hotels]
        return Response({'hotels': data})

class ReservationAPIView(APIView):

    @reservation_list_get_schema
    def get(self, request, pk):
        reservations = Reservations.objects.filter(hotel=pk).order_by('date_start')

        data = [{
            'id': reservation.id,
            'date_start': reservation.date_start,
            'date_end': reservation.date_end,
            'hotel': reservation.hotel.id if reservation.hotel else None 
        } for reservation in reservations] 
        
        return Response({'reservations': data})

    @reservation_list_post_schema
    def post(self, request):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reservation = serializer.save()

        return Response({
            'reservation': {
                'id': reservation.id,
                'date_start': reservation.date_start,
                'date_end': reservation.date_end,
                'hotel': reservation.hotel.id if reservation.hotel else None
            }
        }, status=status.HTTP_201_CREATED)

    @reservation_delete_schema
    def delete(self, request, pk):
        reservations = Reservations.objects.get(pk=pk)
        reservations.delete()
        return Response({"reservation": "Delete reservation №" + str(pk)})