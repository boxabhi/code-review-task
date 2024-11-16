from celery import shared_task
from app.utils.ai_agent import analyze_pr


@shared_task
def analyze_pull_request(repo_url: str, pr_number: int,github_token=None):
    results = analyze_pr(repo_url, pr_number,github_token)
    return results
