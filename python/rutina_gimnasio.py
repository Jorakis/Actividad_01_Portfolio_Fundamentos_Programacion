# # PROGRAMA: Generador de Rutinas de Entrenamiento
# OBJETIVO: Crear rutinas personalizadas leyendo datos de un CSV
# REQUISITOS: 4 funciones Mínimo, manejo de ficheros y validación de datos


import csv  
import os  
import random  


# Lista de grupos musculares que pide la consigna
GRUPOS = ["hombro", "biceps", "triceps", "pecho", "espalda", "pierna", "abdominales"]


def mostrar_menu():
    # Comienza el programa con un menú en el que se le pide al usuario varias opciones: 
    # Crear nueva rutina, Cargar rutina guardada o Salir del Programa
    print("1) Crear nueva rutina")
    print("2) Cargar rutina guardada")
    print("3) Salir del Programa")

#Para crear un nueva rutina de entrenamiento se le preguntará al usuario:
#Cuantos días a la semana va a entrenar [mínimo 3, máximo 5]
#Cuanto tiempo por entrenamiento en minutos [mínimo 45, máximo 90]

def pedir_numero(mensaje, minimo, maximo):
    # Esta funcion pide un numero y obliga a que esté dentro de un rango
    # (por ejemplo lo que estamos trabajando: dias 3-5 o minutos 45-90)
    while True:
        try:
            n = int(input(mensaje).strip())
        except ValueError:
            # Si el usuario no escribe un numero, se vuelve a pedir
            continue

        if minimo <= n <= maximo:
            return n


def leer_ejercicios_csv(ruta_csv):
    # Esta funcion lee el archivo ejercicios.csv
    # y separa los ejercicios por grupo muscular dentro de un diccionario
    ejercicios = {g: [] for g in GRUPOS}

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        for fila in lector:
            # Cada linea debe tener 2 cosas: ejercicio y grupo_muscular
            if len(fila) != 2:
                continue

            ejercicio = fila[0].strip()
            grupo = fila[1].strip()

            # Si hay cabecera "ejercicio,grupo_muscular" la salto
            if ejercicio.lower() == "ejercicio" and grupo.lower() == "grupo_muscular":
                continue

            # Guardo el ejercicio dentro de su grupo (si el grupo es valido)
            if grupo in ejercicios and ejercicio:
                ejercicios[grupo].append(ejercicio)

    return ejercicios


def crear_texto_rutina(dias, minutos, ejercicios):
    # Esta funcion crea el texto final de la rutina
    # La consigna pide que aparezcan todos los grupos musculares en la rutina.
    # Para lograrlo, reparto los grupos en los dias (3 a 5 dias).
    plan = [[] for _ in range(dias)]

    # Reparto todos los grupos entre los dias usando el resto (%)
    for i, grupo in enumerate(GRUPOS):
        plan[i % dias].append(grupo)

    # Presentacion simple (la consigna dice que la presentacion es libre)
    salida = []
    for dia_num, grupos_del_dia in enumerate(plan, start=1):
        salida.append(f"Dia {dia_num}")
        salida.append(f"Tiempo por entrenamiento: {minutos} minutos")

        # Reparto el tiempo del dia entre los grupos del dia (decision libre)
        minutos_por_grupo = minutos // len(grupos_del_dia)

        # Para cada grupo del dia elijo un ejercicio al azar del CSV
        for grupo in grupos_del_dia:
            ejercicio = random.choice(ejercicios[grupo])
            salida.append(f"{grupo}: {ejercicio} ({minutos_por_grupo} min)")

        salida.append("")  # Linea en blanco para separar dias

    return "\n".join(salida).strip()


def guardar_rutina(nombre, texto, carpeta_rutinas):
    # Esta funcion guarda la rutina en un archivo .txt dentro de la carpeta "rutinas"
    os.makedirs(carpeta_rutinas, exist_ok=True)  # Crea la carpeta si no existe
    ruta = os.path.join(carpeta_rutinas, f"{nombre}.txt")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


def cargar_rutina(carpeta_rutinas):
    # Esta funcion permite cargar una rutina guardada:
    # muestra los archivos .txt y deja elegir por numero 1,2,3,...

    if not os.path.isdir(carpeta_rutinas):
        print("No hay rutinas guardadas.")
        return

    # Busco solo archivos .txt dentro de la carpeta rutinas
    archivos = [a for a in os.listdir(carpeta_rutinas) if a.lower().endswith(".txt")]
    archivos.sort()  # Ordeno para que salgan siempre igual

    if not archivos:
        print("No hay rutinas guardadas.")
        return

    # Muestro la lista para que el usuario elija por numero
    for i, nombre in enumerate(archivos, start=1):
        print(f"{i}. {nombre}")

    eleccion = pedir_numero("Elige una rutina por numero: ", 1, len(archivos))
    ruta = os.path.join(carpeta_rutinas, archivos[eleccion - 1])

    # Leo el archivo elegido y lo muestro por consola
    with open(ruta, "r", encoding="utf-8") as f:
        print("")
        print(f.read())
        print("")


def main():
    # Para que funcione en cualquier computadora, uso rutas relativas a este archivo .py
    # Asi en la entrega solo se clona el repo y ejecuta, sin cambiar rutas.
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(carpeta_actual, "ejercicios.csv")
    carpeta_rutinas = os.path.join(carpeta_actual, "rutinas")

    # Cargo los ejercicios desde el CSV al comenzar el programa
    ejercicios = leer_ejercicios_csv(ruta_csv)

    # Bucle principal: mostrar menu y ejecutar la opcion elegida
    while True:
        mostrar_menu()
        opcion = pedir_numero("Selecciona una opcion: ", 1, 3)

        if opcion == 1:
            # La consigna pide preguntar dias (3-5) y minutos (45-90)
            dias = pedir_numero("Cuantos dias a la semana va a entrenar (3-5): ", 3, 5)
            minutos = pedir_numero(
                "Cuanto tiempo por entrenamiento en minutos (45-90): ", 45, 90
            )

            # Creo el texto de la rutina y lo muestro
            rutina = crear_texto_rutina(dias, minutos, ejercicios)
            print("")
            print(rutina)
            print("")

            # Pido un nombre y guardo la rutina en .txt
            nombre = input("Nombre de rutina: ").strip()
            while nombre == "":
                nombre = input("Nombre de rutina: ").strip()

            guardar_rutina(nombre, rutina, carpeta_rutinas)

        elif opcion == 2:
            # Cargar una rutina guardada y mostrarla
            cargar_rutina(carpeta_rutinas)

        elif opcion == 3:
            # Salir del programa
            break


# Esto hace que el programa arranque llamando a main()
if __name__ == "__main__":
    main()
