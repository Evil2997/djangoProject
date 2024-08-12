from .settings import *

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logfile.log',  # Файл лога будет в корне вашего проекта
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'celery': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Если логи не выводятся, попробуй уровень DEBUG / INFO
        },
        'app2': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
