FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY balance/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "balance/manage.py", "runserver", "0.0.0.0:80"]