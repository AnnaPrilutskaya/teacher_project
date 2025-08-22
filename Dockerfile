FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python teacher/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "python teacher/manage.py migrate && gunicorn teacher.wsgi:application --bind 0.0.0.0:$PORT"]