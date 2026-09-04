# Ejercicio 2 

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 1
acceso = False

# 1 Login con máximo 3 intentos sino bloquea la cuenta
while intentos <= 3 and not acceso:
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.\n")
    else:
        print("Error: credenciales inválidas.\n")
        intentos += 1

if not acceso: # por si no logra ingresar despues de los 3 intentos
    print("Cuenta bloqueada")
else: # si ingresa se deplega el menu con este else
    # 2 menu de opciones
    opcion = ""
    while opcion != "4":
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_ingresada = input("Opción: ")

        # Validar que sea numero
        if not opcion_ingresada.isdigit():
            print("Error: ingrese un número válido.\n")
            continue

        # Validar rango 1 a 4
        if int(opcion_ingresada) < 1 or int(opcion_ingresada) > 4:
            print("Error: opción fuera de rango.\n")
            continue

        opcion = opcion_ingresada

        if opcion == "1":
            print("Inscripto\n")

        elif opcion == "2": 
            nueva = input("Nueva clave: ")
            
            while len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva = input("Nueva clave: ")

            confirmacion = input("Confirmar clave: ")
            
            if nueva == confirmacion:
                clave_correcta = nueva # actualiza la clave del inicio
                print("Clave cambiada con éxito.\n")
            else:
                print("Error: las claves no coinciden.\n")
        elif opcion == "3":
            print("Frase motivacional: El éxito es la suma de pequeños esfuerzos.\n")
        elif opcion == "4":
            print("Sesión cerrada.")


