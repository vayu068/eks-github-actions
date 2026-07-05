FROM python:3.12-slim AS base

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-root user with an explicit numeric UID/GID. Kubernetes'
# runAsNonRoot check requires a numeric UID to verify non-root - a named
# user alone isn't enough (kubelet can't resolve /etc/passwd at that point).
RUN addgroup --system --gid 1001 app && adduser --system --uid 1001 --gid 1001 app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER 1001:1001

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
