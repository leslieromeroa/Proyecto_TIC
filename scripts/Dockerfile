FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir psutil pandas requests

RUN mkdir -p /app/results

CMD ["python", "benchmark.py"]
