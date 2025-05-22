import csv
import matplotlib.pyplot as plt

def leer_csv(ruta):
    latencias, cpus, mems = [], [], []
    with open(ruta, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            latencias.append(float(row['latency']))
            cpus.append(float(row['cpu_percent']))
            mems.append(float(row['memory_percent']))
    return latencias, cpus, mems

def estadisticas(datos):
    return {
        'promedio': sum(datos)/len(datos),
        'maximo': max(datos),
        'minimo': min(datos)
    }

ruta_vm = 'results/benchmark_simple_vm.csv'
ruta_docker = 'results/benchmark_simple_docker.csv'

lat_vm, cpu_vm, mem_vm = leer_csv(ruta_vm)
lat_dock, cpu_dock, mem_dock = leer_csv(ruta_docker)

stats_vm = { 'latency': estadisticas(lat_vm),
             'cpu': estadisticas(cpu_vm),
             'mem': estadisticas(mem_vm) }
stats_docker = { 'latency': estadisticas(lat_dock),
                 'cpu': estadisticas(cpu_dock),
                 'mem': estadisticas(mem_dock) }

print("Estadísticas VM:")
for k,v in stats_vm.items():
    print(f"{k}: promedio={v['promedio']:.4f}, max={v['maximo']:.4f}, min={v['minimo']:.4f}")

print("\nEstadísticas Docker:")
for k,v in stats_docker.items():
    print(f"{k}: promedio={v['promedio']:.4f}, max={v['maximo']:.4f}, min={v['minimo']:.4f}")

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(lat_vm, label='Latency VM')
plt.plot(lat_dock, label='Latency Docker')
plt.ylabel('Latency (s)')
plt.legend()

plt.subplot(3,1,2)
plt.plot(cpu_vm, label='CPU VM')
plt.plot(cpu_dock, label='CPU Docker')
plt.ylabel('CPU %')
plt.legend()

plt.subplot(3,1,3)
plt.plot(mem_vm, label='Memory VM')
plt.plot(mem_dock, label='Memory Docker')
plt.ylabel('Memory %')
plt.legend()

plt.xlabel('Mediciones')
plt.tight_layout()
plt.show()
