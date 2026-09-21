lista = [4,3,2,10,9,7,6,6,8,5,6,9,10,8,10]
n = len(lista)
swapped = True
while swapped:
    swapped= False
    for i in range(n-1):
        if lista[i]<lista[i+1]: #Cambiar el signo (> para orden ascendente) (< para orden descendente)
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped = True
print("Orden Descendente: ", lista)    