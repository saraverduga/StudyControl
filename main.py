tareas = []

def agregar_tarea():
    materia = input("Ingrese la materia: ")
    descripcion = input("Ingrese la tarea: ")
    fecha = input("Ingrese la fecha de entrega: ")

    tarea = {
        "materia": materia,
        "descripcion": descripcion,
        "fecha": fecha
    }

    tareas.append(tarea)

    print("\nTarea agregada correctamente.")

def ver_tareas():

    if len(tareas) == 0:
        print("\nNo existen tareas registradas.")

    else:

        print("\nLISTA DE TAREAS")

        for i, tarea in enumerate(tareas, start=1):

            print(f"\nTarea {i}")
            print(f"Materia: {tarea['materia']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha: {tarea['fecha']}")

while True:

    print("\n====== STUDYCONTROL ======")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        agregar_tarea()

    elif opcion == "2":
        ver_tareas()

    elif opcion == "3":
        print("\nGracias por utilizar StudyControl")
        break

    else:
        print("\nOpción inválida")