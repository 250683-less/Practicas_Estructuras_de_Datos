#Practica de laboratorio 
#REGISTRO Y EVALUACIÓN DE CALIFICACIONES

#1. funcion sin parametros
def mostrar_encabezado_escuela():
    print("Universidad Tecnologica de Xicotepec de Juarez")
    print(" REGISTRO Y EVALUACIÓN DE CALIFICACIONES")

#2. funcion sin parametros
def obtener_nota_minima_aprobatoria():
    return 6.0

#3. funcion con 1 parametro
def evaluar_rendimiento(nota_final):
    if nota_final < 6.0: 
        return "Reprobado"
    elif nota_final < 9.5:
        return "Aprobado"
    else:
        return "Excelente"

#4. funcion con 2 parametros
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    nota_final = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(nota_final, 1) 

#5. funcion con 3 parametros e integracion 
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)

    #Mostrar boleta
    mostrar_encabezado_escuela()
    print("\nBOLETA") 
    print("Alumno: ", nombre_alumno)
    print("Nota de exámenes: ", nota_examenes)
    print("Nota de tareas: ", nota_tareas)
    print("Nota final: ", nota_final)
    print("Estado académico: ", estado)

    if nota_final < nota_minima:
        print("Presentar examen extraordinario")
    else: 
        print("No necesita examen extraordinario")


# Ejecución del programa
mostrar_encabezado_escuela()

nombre = input("Ingrese el nombre del alumno: ")
nota_examenes = float(input("Ingrese la nota de exámenes: "))
nota_tareas = float(input("Ingrese la nota de tareas: "))

generar_boleta(nombre, nota_examenes, nota_tareas)
