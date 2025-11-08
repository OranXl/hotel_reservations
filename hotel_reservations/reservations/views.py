from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from mako.testing.exclusions import requires_no_pygments_exceptions
from .models import *


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
    hotel = Hotel.objects.get(pk=pk)
    data = {
        'id': hotel.pk,
        'description': hotel.description,
        'price': hotel.price,
        'created_at': hotel.create_at
    }
    return JsonResponse({'hotels': data})


def add_hotel(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        price = request.POST.get('price')

        hotel = Hotel.objects.create(
            description=description,
            price=price
        )
        return JsonResponse({
            'status': 'success',
            'hotel_id': hotel.id,
            'message': 'Hotel created successfull'
        })


def del_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.delete()
    return HttpResponseRedirect('/hotel')