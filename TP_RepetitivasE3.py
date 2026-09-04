# Ejercicio 3

# Variables individuales para los turnos vacias
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# 1. Pedir nombre del operador y confimamos con .isalpha
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: El nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")

# 2. Menu repetitivo
opcion = ""
while opcion != "5":
    print("\n--- AGENDA DE TURNOS ---")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion_ingresada = input("Opción: ")

    # Validar que sea numero
    while not opcion_ingresada.isdigit():
        print("Error: Ingrese un número válido.")
        opcion_ingresada = input("Opción: ")

    # Validar que este dentro del rango
    while int(opcion_ingresada) < 1 or int(opcion_ingresada) > 5:
        print("Error: Opción fuera de rango.")
        opcion_ingresada = input("Opción: ")

    opcion = opcion_ingresada

    # OPCION 1: RESERVAR TURNO
    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (int(dia) != 1 and int(dia) != 2):
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            # Verificar si ya esta repetido el turno en el dia Lunes
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene un turno reservado para el Lunes.")
            # Guardamos en el primer espacio libre
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado con éxito para {paciente} el Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado con éxito para {paciente} el Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado con éxito para {paciente} el Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado con éxito para {paciente} el Lunes (Turno 4).")
            else:
                print("Error: No hay turnos disponibles para el Lunes.")

        elif dia == "2":
            # Verificar si ya esta repetido en el dia Martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno reservado para el Martes.")
            # Guardamos en el primer espacio libre
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado con éxito para {paciente} el Martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado con éxito para {paciente} el Martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado con éxito para {paciente} el Martes (Turno 3).")
            else:
            
                print("Error: No hay turnos disponibles para el Martes.")

    # OPCION 2: CANCELAR TURNO
    elif opcion == "2":
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (int(dia) != 1 and int(dia) != 2):
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        elif dia == "2":
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de {paciente} cancelado con éxito.")
        else:
            print(f"No se encontró ninguna reserva para {paciente} en el día elegido.")

    # OPCION 3: VER AGENDA DEL DIA
    elif opcion == "3":
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (int(dia) != 1 and int(dia) != 2):
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # OPCION 4: RESUMEN GENERAL
    elif opcion == "4":
        # Conteo Lunes
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        # Conteo Martes
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes: {ocupados_lunes} ocupados | {libres_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados | {libres_martes} disponibles")

        # Determinar dia con mas turnos
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos ocupados: Empate")

    # OPCION 5: CERRAR SISTEMA
    elif opcion == "5":
        print(f"Cerrando sistema. Hasta luego, operador {operador}.")

