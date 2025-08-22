FROM python:3.9-slim

# Сначала рабочая директория
WORKDIR /app

# Копируем ТОЛЬКО requirements.txt сначала
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем ВЕСЬ проект
COPY . .

# Переходим в папку teacher
WORKDIR /app/teacher

# Теперь все команды из правильной директории
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

# Запускаем сервер
CMD ["sh", "-c", "python -m waitress --listen=0.0.0.0:$PORT teacher.wsgi:application"]
