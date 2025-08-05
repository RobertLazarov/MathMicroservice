# MathMicroservice

## Overview

MathMicroservice is a lightweight RESTful API built with FastAPI that performs common mathematical operations and logs each request to a database.

## Features

- Compute power (base^exponent)
- Calculate Fibonacci numbers
- Compute factorial
- Calculate square roots
- View a history of past operations (logs)
- Health check endpoint

## Prerequisites

- Python 3.10 or higher
- (Optional) SQLite for default local database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/MathMicroservice.git
   cd MathMicroservice
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

## Configuration

- To override the database connection URL, set `DATABASE_URL`. By default, a SQLite file `requests.db` is used.

## Running the Service

Start the FastAPI application with Uvicorn:
```bash
uvicorn app.main:app --reload
```
- The API will be available at `http://127.0.0.1:8000`
- You can also run this command to change the port `powershell python -m uvicorn app.main:app --port 8001` (in e.g to run on port 8001).

## Usage

### Web UI
Open your browser and navigate to `http://127.0.0.1:8000` for a simple HTML interface to perform operations and view logs.

### API Endpoints

- POST `/pow`  
  Request body: `{ "base": float, "exponent": float }`

- GET `/fib/{n}`  
  Path parameter: `n` (int)

- GET `/factorial/{n}`  
  Path parameter: `n` (int)

- GET `/sqrt/{x}`  
  Path parameter: `x` (float)

- GET `/logs?limit={limit}`  
  Query parameter: `limit` (int, default 50)

- GET `/health`  
  Returns service status

#### Example cURL requests

Compute power:
```bash
curl -X POST "http://127.0.0.1:8000/pow" \
     -H "Content-Type: application/json" \
     -d '{"base": 2, "exponent": 10}'
```

Fetch Fibonacci:
```bash
curl "http://127.0.0.1:8000/fib/10"
```

Fetch logs:
```bash
curl "http://127.0.0.1:8000/logs?limit=20"
```

## Database

By default, the service uses a SQLite database file `requests.db` in the project root to store request logs. You can change this by setting `DATABASE_URL` in your environment.

