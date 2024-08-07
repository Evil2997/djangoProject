FROM python:3.12-alpine3.19

RUN apk add --no-cache build-base linux-headers

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
