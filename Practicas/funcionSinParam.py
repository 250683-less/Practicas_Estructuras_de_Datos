import random

def lanzar_dado():
    # Elige un número al azar entre 1 y 6
    resultado = random.randint(1, 6)
    print(f"Al lanzar el dado obtuviste un: {resultado}")

lanzar_dado()

import platform

def mostrar_sistema_operativo():
    # Detecta el nombre del sistema operativo
    sistema = platform.system()
    print(f"Estás ejecutando este código en: {sistema}")

mostrar_sistema_operativo()
