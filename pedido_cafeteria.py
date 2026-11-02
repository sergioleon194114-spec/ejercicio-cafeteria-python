# 1. Definir el diccionario con el menú de la cafetería y sus precios
menu = {
    "cafe": 2.50,
    "te": 2.00,
    "pastel": 3.50,
    "sandwich": 5.00
}

# 2. Inicializar la lista vacía para almacenar el pedido del cliente
pedido = []

print("--- ¡Bienvenido a la cafetería! ---")
print("Este es nuestro menú disponible:")
for articulo, precio in menu.items():
    print(f"- {articulo.capitalize()}: ${precio:.2f}")

print("\nEscribe el nombre del artículo que deseas ordenar.")
print("Escribe 'salir' cuando termines tu pedido.\n")

# 3. Bucle para recibir los artículos del cliente
while True:
    item = input("¿Qué deseas ordenar?: ").lower().strip()
    
    if item == 'salir':
        break
    elif item in menu:
        pedido.append(item)
        print(f"-> ¡'{item.capitalize()}' agregado a tu pedido!")
    else:
        print("❌ Lo siento, ese artículo no está en el menú. Inténtalo de nuevo.")

# 4. Generar el recibo formateado con los artículos y el total
print("\n" + "="*30)
print("       RECIBO DE COMPRA")
print("="*30)

total = 0
for item in pedido:
    precio = menu[item]
    print(f"{item.capitalize():<15} ${precio:.2f}")
    total += precio

print("-" * 30)
print(f"TOTAL A PAGAR:  ${total:.2f}")
print("="*30)
print("¡Gracias por tu visita, vuelve pronto!")
