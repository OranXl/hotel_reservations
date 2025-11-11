# hotel_reservations
---Запуск---
    Директория /hotel_reservations/hotel_reservations
    poetry shell
    python manage.py runserver

---Тестирование---
    ---Hotel---
        ---GET---
            http://127.0.0.1:8000/hotel/api
            Выдаёт список всех отелей

            Сортировка
            http://127.0.0.1:8000/hotel/api?sort_by=price&order=asc
            поля для sort_by [create_at, price]
            поля для order [desc, asc]

        ---POST---
            http://127.0.0.1:8000/hotel/api
            Пример запроса
            {
	            "description": "231lnksgbindklv",
                "price": 100
            }
            
        ---DELETE---
            http://127.0.0.1:8000/hotel/api/int
            int - id отеля

    ---Reservations---
        ---GET---
            http://127.0.0.1:8000/reservation/api/int
            int - id отеля

        ---POST---
            http://127.0.0.1:8000/reservation/api
            Пример запроса
            {
                "date_start": "2025-11-10",
                "date_end": "2025-11-11",
                "hotel": 2
            }
            Поля [date_start, date_end] формата ГГГГ-ММ-ДД
        
        ---DELETE---
            http://127.0.0.1:8000/reservation/api/int
            int - id резервации