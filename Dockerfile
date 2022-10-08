FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /balance

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000 'Particular port for Django'

CMD ["python", "manage.py", "runserver"]