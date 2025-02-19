# Gestor de tareas en Python
# Autor: Jonathan

import json

# Funcion para cargar las tareas desde el archivo JSON
def cargar_tareas():
    try:
        with open("tareas.json","r") as archivo:
            return json.load(archivo)      # Carga la lista de tareas archivo JSON
    except FileNotFoundError:
        return []   # Si no existe el archivo, devuelva una lista vacia 

# Funcion para que guarde las tareas en el archivo JSON
def guardar_tareas():
    with open("tareas.json","w") as archivo:
        json.dump(tareas, archivo)

# Lista para almacenar las tareas 
tareas = cargar_tareas()

# Bucle principal del programa 
while True:
    print("\n GESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Mostrar tarea")
    print("3. Marcar tarea como completada")
    print("4. Modificar tareas")
    print("5. Salir")

    opcion = input ("Elige una opcion: ")
    
    if opcion == "1":
        nueva_tarea = input("Escribe la nueva tarea: ")
        tareas.append(nueva_tarea)
        guardar_tareas()
        print(f"Tarea añadida: {nueva_tarea}")
    
    elif opcion == "2":
        if tareas:
            print("\n Lista de tareas")
            for i, tarea in enumerate(tareas,1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas.")
            
    elif opcion == "3":
        if tareas:
            print("\n Lista de tareas: ")
            for i, tarea in enumerate(tareas,1):
                print(f"{i}. {tarea}")
        
            num = int(input("Ingresa el numero de la tarea completada: ")) -1

            if 0<= num < len(tareas):
                tareas_completada = tareas.pop(num)
                guardar_tareas()
                print (f"Tarea completada: {tareas_completada}")
            else:
                print("Numero invalido.")
        else:
            print("No hay tareas para completar.")
    
    elif opcion == "4":
        tareas = cargar_tareas()     # Carga las tareas antes de modificarlas 
        if tareas:
           print("\n Lista de tareas: ")
           for i, tarea in enumerate(tareas,1):
                print(f"{i}. {tarea}")
        
                num = int(input("Ingresa el numero de la tarea a modificar: ")) -1

                if 0 <= num < len(tareas):

                    nueva_tarea = input("Ingresa la nueva descripcion de la tarea: ")
                    tareas[num] = nueva_tarea      # Modifica la tarea en la lista 
                    guardar_tareas()     # Guardamos los cambios en el JSON
                    print(" Tarea modificada con exito.") 
                else:
                     print("Numero invalido.")      
        else:
            print("No hay tareas para modificar.")

    elif opcion == "5":
        print ("Saliendo del programa")
        break # Esto detendra el bucle

    else:
        print ("Opcion no valida. Intentelo de nuevo ")
