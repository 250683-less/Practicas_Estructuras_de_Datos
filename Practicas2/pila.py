
pila_platos = []
print("Paso 1: pila inicializada")
print(f"Pila: {pila_platos}")
print("")


print("Paso: apilar 10 elementos (Push)")
for i in range(1, 11):
    plato = f"Plato {i}"
    pila_platos.append(plato)
    print(f"Se apiló: {plato} -> Pila actual: {pila_platos}")
print()


print("Paso 3: Consultar la cima (Top/Peek)")
plato_actual=pila_platos[-1]
print("El elemeto de la cima es:", plato_actual )
print("")


print("Paso 4: Desapilando 4 elementos (Pop)")
for _ in range(4):
    plato_sacado = pila_platos.pop()
    print(f"Se retiró: {plato_sacado} -> Pila restante: {pila_platos}")
print()



print("Paso 5: Consultar Tamaño")
tamano = len(pila_platos)
print("Tamaño actual de la pila:", tamano)
print("")


print("Extra. Paso 6: Vacias la lista")
#Extra
while pila_platos:
    plato_actual = pila_platos.pop()
    print(f"Saliendo: {plato_actual}. En pila aun: {len(pila_platos)}")
    print("")

print(f"La pila ha siado vaciada por completo. ¿Es vacia?: {len(pila_platos)==0}")
