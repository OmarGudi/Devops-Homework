FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV ENV=production
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers", "2"]