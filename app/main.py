from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI(title="Async Task Processor")

class TaskPayload(BaseModel):
    task_type: str
    payload: dict | None = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

def process_task(task_type: str, payload: dict | None):
    # Simulated background processing
    time.sleep(2)
    print(f"[Worker] Processed task: {task_type}, payload={payload}")

@app.post("/enqueue")
def enqueue_task(data: TaskPayload, bg: BackgroundTasks):
    bg.add_task(process_task, data.task_type, data.payload)
    return {"message": "Task accepted", "task_type": data.task_type}
