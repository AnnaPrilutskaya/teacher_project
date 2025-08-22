FROM python:3.9-slim

WORKDIR /teacher

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "teacher.wsgi:application", "--bind", "0.0.0.0:$PORT"]