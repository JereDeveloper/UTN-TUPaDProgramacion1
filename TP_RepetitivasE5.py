
# Ejercicio 5

# Paso 1: Configuracion del Personaje
print("BIENVENIDO A LA ARENA")
nombre = input("Nombre del Gladiador: ")

# Validación con isalpha() en while, sin try/except
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Paso 2: Inicializacin de Estadisticas (tipos obligatorios solicitados)
vida_jugador = 100       # int
vida_enemigo = 100       # int
pociones = 3             # int
dano_pesado = 15         # int
dano_enemigo = 12        # int
juego_activo = True      # bool
turno_gladiador = True   # bool

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: El Ciclo de Combate
while juego_activo:
    if turno_gladiador:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo})  Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        
        opcion = input("Opción: ")
        
        # Validacion con isdigit() y rango, en while, sin try/except
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Opción inválida. Ingrese 1, 2 o 3.")
            opcion = input("Opción: ")
            
        if opcion == "1":
            dano_final = float(dano_pesado)
            if vida_enemigo < 20:
                # Daño crítico multiplicado por 1.5 (float)
                dano_final = float(dano_pesado * 1.5)
                print("¡Golpe Crítico!")
                
            vida_enemigo -= dano_final
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
            
        elif opcion == "2":
            # Uso de for con range para los 3 golpes rápidos
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
                
        elif opcion == "3":
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te has curado 30 puntos de vida.")
            else:
                print("¡No quedan pociones!")
        
        # Evaluar cambio de turno o fin si el enemigo muere
        if vida_enemigo <= 0:
            juego_activo = False
        else:
            turno_gladiador = False  # Pasa el turno al enemigo
            
    else:
        # Turno del Enemigo (Automático)
        vida_jugador -= dano_enemigo
        print(f"\n¡El enemigo te atacó por {dano_enemigo} puntos de daño!")
        
        # Evaluar cambio de turno o fin si el jugador muere
        if vida_jugador <= 0:
            juego_activo = False
        else:
            turno_gladiador = True   # Vuelve el turno al jugador

# Paso 4: Fin del Juego
print("\n=== FIN DEL JUEGO ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")