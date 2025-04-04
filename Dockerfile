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

# Настроим переменные окружения
ENV PYTHONUNBUFFERED 1

# Собираем статику (если нужно)
RUN python manage.py collectstatic --noinput

# Запускаем сервер разработки Django (только для разработки)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
