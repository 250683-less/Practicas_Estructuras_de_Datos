import time
from collections import deque

cola_turnos = deque()

# Se agregan clientes 
cola_turnos.append(("Turno A01", "ISIDRO ORTIZ RAMIREZ"))
cola_turnos.append(("Turno A02", "GUADALUPE PEREZ DIAZ"))
cola_turnos.append(("Turno A03", "JUANA LAZCANO RODRIGUEZ"))

# Mostrara clientes en espera:
print("Turnos emitidos en la fila del banco:")
for turno, cliente in cola_turnos:
    print(f" - {turno} - {cliente}")

print("\niniciando atencion en ventanilla\n")

while cola_turnos:
    # Desempaqueta el turno y el nombre que sacamos de la cola
    turno_actual, cliente_actual = cola_turnos.popleft()
    
    print(f"Llamando a ventanilla: {turno_actual} - {cliente_actual}")
    time.sleep(1)
    print(f"Atención finalizada: {turno_actual} - {cliente_actual}")
    print(f" (Clientes restantes en la fila: {len(cola_turnos)})")
    print("")

print("Se han atendido todos los turnos. Fila vacía.")
