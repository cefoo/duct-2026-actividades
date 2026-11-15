# Analizador de frecuencias de palabras

Este código procesa el archivo de texto `texto_integradora.txt`, cuenta la frecuencia de cada palabra y genera un gráfico de barras horizontales con las 10 palabras que más se repiten en el archivo. El gráfico de barras se guarda con el nombre `grafico_frecuencias.png`.

## Requisitos

Para ejecutar este código, es necesario tener Python 3 o superior, y se deben instalar las siguientes bibliotecas:

- `matplotlib`
- `pytest`

## Instalación

Para instalar estas bibliotecas, abre la línea de comando y escribe:

```bash
pip install matplotlib pytest
```

O bien:

```bash
python -m pip install matplotlib pytest
```

## Ejecución

El archivo `texto_integradora.txt` tiene que estar en la misma carpeta que el script. Para ejecutar el script principal, escribe en la línea de comando:

```bash
python analizador.py
```

Para ejecutar las pruebas automáticas, escribe:

```bash
pytest
```
