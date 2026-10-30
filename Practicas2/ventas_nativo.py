
# CONTROL DE VENTAS DE UNA TIENDA

# METODO 2: UTILIZANDO PYTHON NATIVO

# Matrices como listas
A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]

# Sumar las matrices
total = [
    [A[i][j] + B[i][j] for j in range(2)] #A[i][j] accede a un elemento de la matriz indicando su fila y columna
    for i in range(2)
]

# Calcula ingresos
ingreso = [
    [total[i][j] * 50 for j in range(2)]
    for i in range(2)
]

print("VENTAS CON PYTHON NATIVO")
print("Total de productos: (Sábado + Domingo)")
print(total)

print("Ingreso total en pesos: (a 50 pesos por producto)")
print(ingreso)
