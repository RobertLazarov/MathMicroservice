from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api import api_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Math Operations Service",
    version="1.0.0",
    description="Compute power, Fibonacci, factorial, sqrt; audit every request.",
)

app.include_router(api_router)

@app.get("/", response_class=HTMLResponse, summary="Landing page with HTML UI")
async def root():
    return """
    <html>
    <head>
      <title>Math Ops UI</title>
      <style>
        body { font-family: sans-serif; padding: 1em; }
        form, div { margin-bottom: 1em; }
        button { margin-left: 0.5em; }
      </style>
    </head>
    <body>
      <h1>Math Operations</h1>

      <form onsubmit="compute(event, '/pow', ['base','exponent'], 'POST')">
        <h2>Power</h2>
        Base: <input type="number" step="any" name="base" required>
        Exponent: <input type="number" step="any" name="exponent" required>
        <button type="submit">Compute</button>
      </form>

      <form onsubmit="compute(event, '/fib', ['n'], 'GET')">
        <h2>Fibonacci</h2>
        n: <input type="number" name="n" required>
        <button type="submit">Compute</button>
      </form>

      <form onsubmit="compute(event, '/factorial', ['n'], 'GET')">
        <h2>Factorial</h2>
        n: <input type="number" name="n" required>
        <button type="submit">Compute</button>
      </form>

      <form onsubmit="compute(event, '/sqrt', ['x'], 'GET')">
        <h2>Square Root</h2>
        x: <input type="number" step="any" name="x" required>
        <button type="submit">Compute</button>
      </form>

      <div>
        <h2>View Logs</h2>
        <label for="logLimit">Number of logs:</label>
        <input type="number" id="logLimit" min="1" max="100" value="50">
        <button onclick="loadLogs()">Load Logs</button>
      </div>

      <pre id="result"></pre>

      <script>
      async function compute(event, path, fields, method) {
        event.preventDefault();
        document.getElementById('result').textContent = '';
        const form = event.target;
        const data = {};
        fields.forEach(f => data[f] = form.elements[f].value);
        let url = path;
        let options = {};
        if (method === 'GET') {
          url = `${path}/${encodeURIComponent(data[fields[0]])}`;
        } else {
          options = { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) };
        }
        const res = await fetch(url, options);
        const out = await res.json();
        document.getElementById('result').textContent = JSON.stringify(out, null, 2);
      }

      async function loadLogs() {
        const limit = document.getElementById('logLimit').value;
        const res = await fetch(`/logs?limit=${limit}`);
        const logs = await res.json();
        document.getElementById('result').textContent = JSON.stringify(logs, null, 2);
      }
      </script>
    </body>
    </html>
    """


@app.get("/health", summary="Health check")
async def health():
    with engine.connect() as conn:
        conn.execute("SELECT 1")
    return {"status": "ok"}
