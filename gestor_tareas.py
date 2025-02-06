# Gestor de tareas en Python
# Autor: Jonathan

# Lista para almacenar las tareas 
tareas = []

# Bucle principal del programa 
while True:
    print("\n GESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Mostrar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    
    opcion = input ("Elige una opcion: ")
    
    if opcion == "1":
        nueva_tarea = input("Escribe la nueva tarea: ")
        tareas.append(nueva_tarea)
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
                print (f"Tarea completada: {tareas_completada}")
            else:
                print("Numero invalido.")
        else:
            print("No hay tareas para completar.")
        
    elif opcion == "4":
        print ("Saliendo del programa")
        break # Esto detendra el bucle
    else:
        print ("Opcion no valida. Intentelo de nuevo ")
