from celery import Celery

from app.core.config import settings

celery = Celery('tasks')
celery.config_from_object({
    'broker_url': settings.redis_url,
    'result_backend': settings.redis_url,
    'task_serializer': 'json',
    'accept_content': ['json'],
    'result_serializer': 'json',
})
celery.autodiscover_tasks(['app.tasks'])
