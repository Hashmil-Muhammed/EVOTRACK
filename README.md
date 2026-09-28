# EV Battery Log

A premium, local-first web application for tracking EV battery charging and driving history.

## Features
- Notion/Airtable style premium UI
- Single-page interface focused on speed
- Real-time inline editing
- Local SQLite database persistence
- CSV Export

## Tech Stack
- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: HTML5, Vanilla JavaScript, Custom CSS

## Installation & Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment (Windows):
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --reload
```

5. Open your browser:
Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints
- `GET /api/logs`: Fetch all logs
- `POST /api/logs`: Create a new log
- `PATCH /api/logs/{id}`: Update specific fields of a log
- `DELETE /api/logs/{id}`: Delete a log
