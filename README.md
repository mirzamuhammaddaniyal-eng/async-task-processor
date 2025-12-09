# async-task-processor

A simple asynchronous task processing microservice built with **FastAPI**, demonstrating background task execution, lightweight worker simulation, and production-ready API patterns.

## Features
- `/enqueue` endpoint to accept and queue simulated background tasks.
- `/health` endpoint for basic uptime monitoring.
- Background task execution using FastAPI’s `BackgroundTasks`.
- Simple worker loop (`worker.py`) to simulate a backend processor.
- Clean, modular structure that mirrors real microservice design.

---

## Tech Stack
- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- BackgroundTasks (async processing)

---

## Project Structure
```text
async-task-processor/
│
├── app/
│   ├── main.py
│   └── worker.py
│
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/async-task-processor.git
cd async-task-processor
```

```bash
# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

```bash
# 3. Install dependencies
pip install -r requirements.txt
```

```bash
# 4. Start the API server
uvicorn app.main:app --reload
```

Visit:
```
http://127.0.0.1:8000
```

Health check:
```
/health
```

Enqueue a task (example JSON):
```
POST http://127.0.0.1:8000/enqueue
{
  "task_type": "email",
  "payload": {"to": "user@example.com"}
}
```
