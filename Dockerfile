# Використовуємо офіційний Python-образ
FROM python:3.11-slim

# Змінні середовища
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Робоча директорія
WORKDIR /app

# Копіюємо файли проєкту в контейнер
COPY . /app/

# Встановлюємо pip і залежності
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Команда запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
