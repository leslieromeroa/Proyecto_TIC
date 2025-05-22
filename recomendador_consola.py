import requests

def obtener_recomendaciones(genero, artista):
    if not genero and not artista:
        print("Por favor, ingresa al menos un género o un artista.")
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
                print("\n🎵 Recomendaciones:")
                for item in datos["data"]:
                    print(f"- {item['title']} - {item['artist']['name']}")
            else:
                print("No se encontraron recomendaciones para esa consulta.")
        else:
            print("Error al obtener recomendaciones. Inténtalo de nuevo más tarde.")
    except requests.exceptions.RequestException:
        print("Error de conexión. Verifica tu internet.")

# Modo consola
if __name__ == "__main__":
    print("🎧 Bienvenido al Recomendador de Música 🎶")
    genero = input("Ingresa un género musical (opcional): ").strip()
    artista = input("Ingresa un artista (opcional): ").strip()
    obtener_recomendaciones(genero, artista)
