from fastapi import APIRouter, HTTPException
from celery.result import AsyncResult
from app.tasks.review_task import analyze_pull_request
from app.models.task_result import get_task_result
from pydantic import BaseModel, HttpUrl
from typing import Optional

router = APIRouter()

class AnalyzePRRequest(BaseModel):
    repo_url: HttpUrl
    pr_number: int
    github_token: Optional[str] = None

class AnalyzePRResponse(BaseModel):
    task_id: str
    status: str


@router.post("/analyze-pr")
def analyze_pr(payload: AnalyzePRRequest):
    task = analyze_pull_request.apply_async(args=[
        payload.repo_url, 
        payload.pr_number,
        payload.github_token])
    
    return AnalyzePRResponse(task_id=task.id, status="submitted")


@router.get("/status/{task_id}")
def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    
    if task_result.state == 'PENDING':
        return {"status": "Pending or Task not found"}
    elif task_result.state == 'STARTED':
        return {"status": "In Progress"}
    elif task_result.state == 'SUCCESS':
        return {
            "status": "Completed",
            "result": task_result.result  # Access the stored result
        }
    elif task_result.state == 'FAILURE':
        return {
            "status": "Failed",
            "error": str(task_result.result)
        }
    else:
        return {"status": task_result.state}

@router.get("/results/{task_id}")
def get_results(task_id: str):
    result = get_task_result(task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task results not found")
    return result
