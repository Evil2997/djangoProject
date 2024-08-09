#!/bin/sh

# Проверка доступности Redis перед запуском Celery worker и beat
while ! nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 1
done

exec "$@"
