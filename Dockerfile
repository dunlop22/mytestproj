# Используем официальный Python образ
FROM python:3.9-slim

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG SECRET_KEY

# Настроим переменные окружения
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False
ENV SECRET_KEY=${SECRET_KEY}
ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}


# Собираем статику (если нужно)
RUN python manage.py collectstatic --noinput

# Запускаем сервер разработки Django (только для разработки)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
