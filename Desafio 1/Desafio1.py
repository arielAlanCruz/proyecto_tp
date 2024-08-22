import random

def imprimir(matriz,estudiantes,materias):
    # Imprimir la matriz con etiquetas de estudiantes y materias
    print("\nMatriz de Calificaciones:")
    print("     ", end="")
    for i in range(len(materias)):
        print("%4s" % materias[i], end=" ")
    print()
    for fil in range(len(estudiantes)):
        print("%4s" % estudiantes[fil], end=" ")
        for col in range(len(materias)):
            print("%4d" % matriz[fil][col], end=" ")
        print() 

def promedioEstudiante(matriz):
    promedioEst=[]
    filas=len(matriz)
    columnas=len(matriz[0])
    for fil in range(filas):
        sumNotas=0
        for col in range(columnas):
            sumNotas=sumNotas+matriz[fil][col]
        #calcular promedio y y guardar en promedios
        promedio=sumNotas/columnas
        promedioEst.append(promedio)
    i=0
    while i<filas:
        print("Promedio notas de est",i+1,":",promedioEst[i])
        i=i+1

def promedioMaterias(matriz):
    promedioMateria=[]
    filas=len(matriz)
    columnas=len(matriz[0])

    for col in range(columnas):
        sumNotas=0
        for fil in range(filas):
            sumNotas=sumNotas+matriz[fil][col]
        #calcular promedio y y guardar en promedios    
        promedio=sumNotas/filas
        promedioMateria.append(promedio)
    i=0
    while i<columnas:
        
        print("Promedio notas de materia",i+1,":",promedioMateria[i])
        i=i+1   


estudiantes = ["est1", "est2", "est3", "est4", "est5"]
materias = ["Mat1", "Mat2", "Mat3", "Mat4"]

filas = len(estudiantes)      
columnas = len(materias)

matriz = []

# creamos la matriz con ceros.
for fil in range(filas):
    matriz.append([0] * columnas)

# cargamos aleatoriamente la matriz
for fil in range(filas):
    for col in range(columnas):
        matriz[fil][col] = random.randint(1,10)

imprimir(matriz,estudiantes,materias)
promedioEstudiante(matriz)
print()
promedioMaterias(matriz)
