from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Task
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, date

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Intelligent To-Do Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    if not title.strip():
        raise HTTPException(status_code=400, detail="Task title cannot be empty")

    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.put("/tasks/{task_id}")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = True
    db.commit()
    return {"message": "Task completed"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}

# ✅ Daily productivity endpoint
@app.get("/productivity/daily")
def daily_productivity(db: Session = Depends(get_db)):
    today = date.today()

    tasks = db.query(Task).all()

    today_tasks = [
        t for t in tasks
        if t.created_at.date() == today
    ]

    total = len(today_tasks)
    completed = len([t for t in today_tasks if t.completed])

    percentage = (completed / total * 100) if total > 0 else 0

    return {
        "completed": completed,
        "total": total,
        "percentage": round(percentage, 2)
    }
