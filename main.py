from flask import Flask, request
from datetime import datetime

# get current datetime
dt = datetime.now()

x = dt.strftime('%A')

app = Flask(__name__)


@app.get("/")
def hello():
    return f"What an beautiful spring day {x} is!\n"


if __name__ == "__main__":
    # Development only: run "python main.py" and open http://localhost:8080
    # When deploying to Cloud Run, a production-grade WSGI HTTP server,
    # such as Gunicorn, will serve the app.
    app.run(host="localhost", port=8080, debug=True)
