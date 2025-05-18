# Imagen base de Python
FROM python:3.10-slim

# Crear carpeta en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar psutil
RUN pip install psutil

# Crear carpeta de resultados si no existe
RUN mkdir -p results

# Comando por defecto al ejecutar el contenedor
CMD ["python", "benchmark.py"]
