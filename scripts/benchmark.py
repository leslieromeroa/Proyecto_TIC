import requests
import time
import csv
import psutil
import os
import sys

duration = 10  # segundos (para hacer pruebas rápidas)
end_time = time.time() + duration
results = []

print("⏳ Ejecutando benchmark por 10 segundos...")

while time.time() < end_time:
    start = time.time()
    try:
        latency = time.time() - start
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        results.append([latency, cpu, mem])
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.2)

env_label = 'docker'
if len(sys.argv) > 1 and sys.argv[1].lower() == 'vm':
    env_label = 'vm'

filename = f"benchmark_simple_{env_label}.csv"
os.makedirs("results", exist_ok=True)
filepath_csv = f"results/{filename}"

with open(filepath_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

print(f"✅ Benchmark terminado. Archivo guardado en {filepath_csv}")
