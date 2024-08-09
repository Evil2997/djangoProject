#!/bin/sh

# Ожидание доступности RabbitMQ перед запуском сервиса
until nc -z rabbitmq 5672; do
  echo "Waiting for RabbitMQ..."
  sleep 2
done

exec "$@"
