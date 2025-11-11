from django.urls import path

from . import views

urlpatterns = [
    # Hotel
    path('hotel', views.hotel_list, name='hotels'),
    path('hotel/<int:pk>', views.detail_hotel, name='detail_hotel'),
    path('hotel/<int:pk>/delete', views.del_hotel, name='del_hotel'),

    # Reservations
    path('reservation', views.res_list, name='reservations'),
    path('reservation/<int:pk>', views.res_hotel_detail, name='res_hotel_detail'),
    path('reservation/<int:pk>/delete', views.res_del, name='reservations_del'),
    # API
    path('hotel/api', views.HotelAPIView.as_view()),
    path('reservation/api', views.ReservationAPIView.as_view()),
]