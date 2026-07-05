"""Minimal Flask application used to demonstrate a GitHub Actions ->
ECR -> EKS deployment pipeline.

Endpoints:
  GET /        - returns a small JSON payload including the pod hostname,
                 so you can see traffic being spread across replicas.
  GET /health  - liveness/readiness probe target.
"""
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "dev")


@app.get("/")
def index():
    return jsonify(
        message="Hello from the GitHub Actions -> ECR -> EKS demo app!",
        hostname=socket.gethostname(),
        version=APP_VERSION,
    )


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # Only used for local development. In the container, gunicorn serves the app.
    app.run(host="0.0.0.0", port=8080)
