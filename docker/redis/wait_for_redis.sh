#!/bin/sh

# Ожидание доступности Redis перед запуском сервиса
until nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 5
done

exec "$@"
