# CONTROL DE VENTAS DE UNA TIENDA

# METODO 1: UTILIZANDO NUMPY
import numpy as np

# Matrices de ventas
A = np.array([[10, 15], [20, 5]])
B = np.array([[5, 12], [15, 8]])

# Sumar las ventas
total = A + B

# Calcular ingresos
ingreso = total * 50

print("VENTAS CON NUMPY")
print("Total de productos: (Sábado + Domingo)")
print(total)

print("Ingreso total en pesos: ( a 50 pesos por producto)")
print(ingreso)