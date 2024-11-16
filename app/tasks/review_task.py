from celery import shared_task
from app.utils.ai_agent import analyze_pr


from celery import Celery

# Configure Celery
celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",  # Redis as the message broker
    backend="redis://redis:6379/0" # Redis for task result backend
)
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@shared_task
def analyze_pull_request(repo_url: str, pr_number: int,github_token=None):
    results = analyze_pr(repo_url, pr_number,github_token)
    return results


