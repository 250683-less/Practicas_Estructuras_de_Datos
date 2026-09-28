def crear_usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Usando parámetros posicionales
usuario1 = crear_usuario("Ana", 25, "Cancun")

# Usando parámetros con nombre (más claro)
usuario2 = crear_usuario(nombre="Carla", edad=30, ciudad="Chiapas")

# Puedes cambiar el orden si usas nombres
usuario3 = crear_usuario(ciudad="Colombia", nombre="Laura", edad=28)

print(usuario1)  # Ana, 25 años, de Madrid
print(usuario2)  # Carlos, 30 años, de Barcelona
print(usuario3)  # Laura, 28 años, de Valencia


def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area

# Llamar a la función
resultado = calcular_area_rectangulo(5, 10)
print(f"El area del rectangulo 1: {resultado}" )  # Salida: 50

# El orden importa
resultado2 = calcular_area_rectangulo(20, 10)
print(f"El area del rectangulo 2: {resultado2}" )  # Salida: 50 (mismo resultado en este caso)