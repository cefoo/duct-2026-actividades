from analizador import contar_frecuencias

# Nota: Para las pruebas, usamos cadenas cortas con palabras representativas que forman parte del corpus (texto_integradora.txt).

def test_frecuencias_basico():
    resultado = contar_frecuencias("pueblo mercado pueblo")
    assert resultado["pueblo"] == 2
    assert resultado["mercado"] == 1

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Pueblo pueblo PUEBLO")
    assert resultado["pueblo"] == 3