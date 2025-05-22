import tkinter as tk
from tkinter import Canvas
import requests

def obtener_recomendaciones():
    genero = entry_genero.get()
    artista = entry_artista.get()
    
    if not genero and not artista:
        resultado_label.config(text="Por favor, ingresa al menos un género o un artista.")
        return

    url = "https://api.deezer.com/search"
    consulta = ""
    if genero:
        consulta += f"{genero} "
    if artista:
        consulta += f"{artista}"
    
    parametros = {
        "q": consulta.strip(),
        "limit": 5
    }
    
    try:
        respuesta = requests.get(url, params=parametros)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos.get("data"):
                recomendaciones = [f"{item['title']} - {item['artist']['name']}" for item in datos["data"]]
                resultado_label.config(text="Recomendaciones:\n" + "\n".join(recomendaciones))
            else:
                resultado_label.config(text="No se encontraron recomendaciones para esa consulta.")
        else:
            resultado_label.config(text="Error al obtener recomendaciones. Inténtalo de nuevo más tarde.")
    except requests.exceptions.RequestException:
        resultado_label.config(text="Error de conexión. Verifica tu internet.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Recomendador de Música")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Crear canvas para el fondo degradado
canvas = Canvas(ventana, width=500, height=400)
canvas.pack(fill="both", expand=True)

def crear_degradado(canvas, color1, color2, steps):
    for i in range(steps):
        r1, g1, b1 = ventana.winfo_rgb(color1)
        r2, g2, b2 = ventana.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / steps) // 256
        g = int(g1 + (g2 - g1) * i / steps) // 256
        b = int(b1 + (b2 - b1) * i / steps) // 256
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_rectangle(0, i * 10, 500, (i + 1) * 10, outline="", fill=hex_color)

# Fondo degradado: negro a morado
crear_degradado(canvas, "#000000", "#800080", 40)

# Crear frame centrado con fondo negro
frame = tk.Frame(canvas, bg='#000000', bd=0)
canvas.create_window(250, 200, window=frame)

# Estilos
estilo_entrada = {"font": ("Arial", 12), "justify": "center"}
estilo_etiqueta = {"bg": "#000000", "fg": "white", "font": ("Arial", 12), "justify": "center"}
estilo_boton = {"bg": "#B57EDC", "fg": "black", "font": ("Arial", 12, "bold")}

# Etiquetas y entradas
label_genero = tk.Label(frame, text="Género:", **estilo_etiqueta)
label_genero.pack(pady=5)

entry_genero = tk.Entry(frame, **estilo_entrada)
entry_genero.pack(pady=5, ipadx=30)

label_artista = tk.Label(frame, text="Artista:", **estilo_etiqueta)
label_artista.pack(pady=5)

entry_artista = tk.Entry(frame, **estilo_entrada)
entry_artista.pack(pady=5, ipadx=30)

# Botón de búsqueda
buscar_button = tk.Button(frame, text="Buscar Recomendaciones", command=obtener_recomendaciones, **estilo_boton)
buscar_button.pack(pady=15)

# Resultado
resultado_label = tk.Label(frame, text="", wraplength=400, **estilo_etiqueta)
resultado_label.pack(pady=10)

ventana.mainloop()
