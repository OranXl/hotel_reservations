from django.urls import path

from . import views

urlpatterns = [
    path('hotel', views.hotel, name='hotels'),
    path('hotel/<int:pk>', views.detail_hotel, name='detail_hotel'),
    path('hotel/add', views.add_hotel, name='add_hotel'),
    path('hotel/<int:pk>/delete', views.del_hotel, name='del_hotel'),
]