import matplotlib.pyplot as plt

def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto por analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def analizar_y_graficar(ruta, top_n=10):
    """
    Lee un archivo de texto, cuenta la frecuencia de cada palabra
    y genera un gráfico de barras horizontales con las top_n
    palabras más frecuentes.

    Parametros:
        ruta (str): ruta al archivo de texto por analizar
        top_n (int): cantidad de palabras por graficar

    Retorna:
        None (genera y guarda el gráfico)

    Nota: Para jugar un poco, personalicé el color de las barras
    tomando como referencia los colores disponibles en
    https://matplotlib.org/stable/gallery/color/named_colors.html
    """

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return

    palabras_texto = texto.lower().split()
    frecuencias = {}
    for palabra in palabras_texto:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="darkorchid")
    plt.title(f"Top {top_n} palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()

def main():
    analizar_y_graficar("texto_integradora.txt")

if __name__ == "__main__":
    main()