# FastAPI with Celery and Redis Integration

This project demonstrates how to integrate **FastAPI** with **Celery** for asynchronous task processing and **Redis** as the message broker and result backend.

---

## Features

- **FastAPI** for building a modern, high-performance web API.
- **Celery** for managing background tasks.
- **Redis** as the message broker and task result backend.
- Asynchronous processing of long-running tasks.
- RESTful endpoints to trigger tasks and retrieve task statuses.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.10+ 
- Redis server
- Pipenv or `pip` for dependency management

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/boxabhi/code-review-task
   cd code-review-task
   docker-compose up --build
   ```

2. Access the Application
    ```bash
    Once the containers are up, the FastAPI application will be available at:

    Copy code
    http://127.0.0.1:8000/docs
    Use this URL to interact with the API and view the auto-generated Swagger documentation.

    ```

2. Api endpoints 
    ```bash
    1. http://127.0.0.1:8001/analyze-pr
    body -
    {
    "repo_url" : "https://github.com/boxabhi/MyCurrency",
    "pr_number" : 1
    }

    2. http://127.0.0.1:8001/status/{task_id}/
    ```

3. This Application uses Groq to run llma model 
    groq API key you can generate from 

    https://console.groq.com/login

    mention API in ai_agent.py
    

