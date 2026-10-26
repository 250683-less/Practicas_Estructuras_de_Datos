import numpy as np
#Matriz A y B
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
#SUMA ELEMENTOS
suma=A+B
print("--SUMA (A+B)--")
print(suma)
#MULTIPLICACION DE ELEMENTOS
prod_elem=A*B
print("--MULTIPLICACION (AxB)--")
print(prod_elem)
#PRODUCTO MATRICIAL
prod_mat=A@B
print("--PRODUCTO MATRICIAL (A@B)--")
print(prod_mat)
#TRANSPUESTA
transpuesta=A.T
print("--TRANSPUESTA DE A (A-T)--")
print(transpuesta)
# DETERMINANTE E INVERSA (Corregido)
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A) # Cambiado B por A para coincidir con tus prints
print("--DETERMINANTE DE A--")
print(det_A)
print("--INVERSA DE A--")
print(inv_A)