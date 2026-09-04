
# Ejercicio 1
# 1 Le pedimos el nombre al cliente y vemos si son letras
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Cliente: ")

# 2 Pedimos cantidad de productos y vemos si es numeros 
cantidad_ingresado = input("Cantidad de productos: ")
while not cantidad_ingresado.isdigit() or int(cantidad_ingresado) <= 0:
    print("Error: Ingrese un número entero positivo mayor a 0.")
    cantidad_ingresado = input("Cantidad de productos: ")

cantidad_productos = int(cantidad_ingresado)

total_sin_descuento = 0
total_con_descuento = 0

# 3 Procesamos cada producto con un ciclo for
for i in range(1, cantidad_productos + 1):
    print(f"\nProducto {i}")
    
    # Validamos precio con numeros enteros validos
    precio_ingresado = input("Precio: ")
    while not precio_ingresado.isdigit():
        print("Error: Ingrese un precio entero válido.")
        precio_ingresado = input("Precio: ")
        
    precio = int(precio_ingresado)
    
    # Validamos opción de descuento 
    tiene_descuento = input("Descuento (S/N): ").lower()
    while tiene_descuento not in ['s', 'n']:
        print("Error: Ingrese 'S' o 'N'.")
        tiene_descuento = input("Descuento (S/N): ").lower()
    
    # Acumulamos subtotales
    total_sin_descuento += precio
    
    if tiene_descuento == 's':
        total_con_descuento += precio * 0.90
    else:
        total_con_descuento += precio

# 4 Cálculomos de resultados
ahorro_total = total_sin_descuento - total_con_descuento
promedio_por_producto = total_con_descuento / cantidad_productos

# 5 imprimimos
print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")