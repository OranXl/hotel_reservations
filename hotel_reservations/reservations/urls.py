from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Любой текст",
        default_version="v 0.0.1",
        description="Документация по API к ресурсу",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="demuratov12@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


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
    path('hotel/api/<int:pk>', views.HotelAPIView.as_view()),
    path('reservation/api', views.ReservationAPIView.as_view()),
    path('reservation/api/<int:pk>', views.ReservationAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]