from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class TaskResult(Base):
    __tablename__ = "task_results"
    task_id = Column(String, primary_key=True, index=True)
    results = Column(Text)



def save_task_result(task_id, results):
    session = SessionLocal()
    task_result = TaskResult(task_id=task_id, results=str(results))
    session.add(task_result)
    session.commit()
    session.close()

def get_task_result(task_id):
    session = SessionLocal()
    result = session.query(TaskResult).filter(TaskResult.task_id == task_id).first()
    session.close()
    return result
