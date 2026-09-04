
# Ejercicio 4 

# Variables iniciales (NO se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Variable adicional para la regla anti-spam
forzar_seguidas = 0

# 1. Pedir nombre del agente y validar
agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: El nombre debe contener solo letras.")
    agente = input("Nombre del agente: ")

# 2. Menu de acciones (Ciclo principal del juego)
juego_activo = True

while juego_activo and energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    # Evaluar regla de bloqueo por alarma antes de mostrar el menú
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        juego_activo = False
        

    # Mostrar estado actual
    print(f"\n--- ESTADO DEL AGENTE {agente.upper()} ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    opcion = input("Elige una acción (1, 2 o 3): ")
    
    # Validar opcion del menu
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Opción inválida. Ingrese un número entre 1 y 3.")
        opcion = input("Elige una acción (1, 2 o 3): ")
        
    if opcion == "1":
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        # Regla anti-spam
        if forzar_seguidas >= 3:
            print("¡Regla anti-spam! La cerradura se trabó por forzarla demasiado. Alarma activada.")
            alarma = True
        else:
            if energia < 40:
                print("¡Riesgo de alarma por baja energía!")
                num = input("Ingresa un número del 1 al 3: ")
                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    print("Error: Ingrese un número válido (1, 2 o 3).")
                    num = input("Ingresa un número del 1 al 3: ")
                    
                if num == "3":
                    alarma = True
                    print("¡Has activado la alarma!")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Lograste abrir una cerradura!")
            else:
                print("La alarma está encendida, no pudiste abrir la cerradura.")

    elif opcion == "2":
        forzar_seguidas = 0  # Corta racha de forzar
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        
        # Bucle for de 4 pasos mostrando progreso
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""  # Se reinicia el codigo tras lograr abrir
            print("¡Hackeo completo! Se abrió una cerradura automáticamente.")
            
    elif opcion == "3":
        forzar_seguidas = 0  # Corta racha de forzar
        energia += 15
        if energia > 100:
            energia = 100  # Maximo de energia permitido
        tiempo -= 1
        
        if alarma == True:
            energia -= 10
            
        print("Descansaste y recuperaste energía.")

# 3. Condiciones de fin
print("\n=== FIN DE LA PARTIDA ===")
if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA (bloqueo). El sistema de la bóveda se bloqueó por completo.")
elif cerraduras_abiertas >= 3:
    print("¡VICTORIA! Has abierto la boveda con éxito.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te has quedado sin energía o sin tiempo.")