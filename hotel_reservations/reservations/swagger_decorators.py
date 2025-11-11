from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Декораторы для HotelAPIView
hotel_list_get_schema = swagger_auto_schema(
    operation_description="Получить список всех номеров отеля с сортировкой",
    manual_parameters=[
        openapi.Parameter(
            'sort_by', openapi.IN_QUERY,
            description="Поле для сортировки (price, created_at)",
            type=openapi.TYPE_STRING,
            enum=['price', 'created_at', 'create_at'],
            default='created_at'
        ),
        openapi.Parameter(
            'order', openapi.IN_QUERY,
            description="Порядок сортировки",
            type=openapi.TYPE_STRING,
            enum=['asc', 'desc'],
            default='desc'
        )
    ],
    responses={
        200: openapi.Response(
            description="Список отелей",
            examples={
                "application/json": {
                    "hotels": [
                        {
                            "id": 1,
                            "description": "Прекрасный номер с видом на море",
                            "price": "150.00",
                            "create_at": "2024-01-15T10:30:00Z"
                        }
                    ]
                }
            }
        )
    }
)

hotel_list_post_schema = swagger_auto_schema(
    operation_description="Создать новый номер отеля",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['description', 'price'],
        properties={
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={
        201: openapi.Response(
            description="Отель создан",
            examples={
                "application/json": {
                    "hotel": {
                        "id": 1,
                        "description": "Новый отель",
                        "price": "200.00",
                        "create_at": "2024-01-15T10:30:00Z"
                    }
                }
            }
        )
    }
)

# Декораторы для ReservationAPIView
reservation_list_get_schema = swagger_auto_schema(
    operation_description="Получить список бронирований (отсортированы по дате начала)",
    manual_parameters=[
        openapi.Parameter(
            'room_id', openapi.IN_QUERY,
            description="ID номера отеля для фильтрации",
            type=openapi.TYPE_INTEGER
        )
    ],
    responses={
        200: openapi.Response(
            description="Список бронирований",
            examples={
                "application/json": {
                    "reservations": [
                        {
                            "id": 1,
                            "date_start": "2024-12-30",
                            "date_end": "2024-12-31",
                            "hotel": 1
                        }
                    ]
                }
            }
        )
    }
)

reservation_list_post_schema = swagger_auto_schema(
    operation_description="Создать новое бронирование",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['date_start', 'date_end', 'hotel'],
        properties={
            'date_start': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
            'date_end': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
            'hotel': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
    responses={
        201: openapi.Response(
            description="Бронирование создано",
            examples={
                "application/json": {
                    "reservation": {
                        "id": 1,
                        "date_start": "2024-12-30",
                        "date_end": "2024-12-31",
                        "hotel": 1
                    }
                }
            }
        )
    }
)

# Декораторы для удаления
hotel_delete_schema = swagger_auto_schema(
    operation_description="Удалить номер отеля и все его бронирования",
    responses={
        204: "Отель удален",
        404: "Отель не найден"
    }
)

reservation_delete_schema = swagger_auto_schema(
    operation_description="Удалить бронирование",
    responses={
        204: "Бронирование удалено",
        404: "Бронирование не найдено"
    }
)