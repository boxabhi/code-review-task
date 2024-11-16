from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="Code Quality Analyzer",
    description="Analyze GitHub repository code quality using AI.",
    version="1.0.0"
)





app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Autonomous Code Review Agent"}
