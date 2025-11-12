FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* README.md /app/

RUN poetry config virtualenvs.create false

# Устанавливаем зависимости БЕЗ установки текущего проекта
RUN poetry install --without dev --no-root --no-interaction --no-ansi

# Затем копируем остальные файлы проекта
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]