from celery import Celery

# Configure Celery
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Redis as the message broker
    backend="redis://localhost:6379/0" # Redis for task result backend
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app.conf.result_expires = 86400
