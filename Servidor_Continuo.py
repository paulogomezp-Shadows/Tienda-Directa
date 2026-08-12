print("📱 Servidor de la Tienda Oficial INICIADO 📱")
print("Esperando conexiones de clientes...\n")

# Todo lo que esté dentro de este 'while True' se repetirá infinitamente
while True:
    print("\n--- NUEVA COMPRA ---")
    
    # 1. Capturamos el primer dato.
    cliente_nombre = input("Ingresa tu nombre (o escribe 'salir' para apagar el sistema): ")
    
    # 2. El botón de apagado de emergencia
    if cliente_nombre.lower() == "salir":
        print("Apagando el servidor... ¡Buenas noches!")
        break  # Esto rompe el bucle infinito y termina el programa
        
    # 3. Si no escribió 'salir', el programa continúa pidiendo los datos
    cliente_direccion = input("Ingresa tu dirección exacta para el envío: ")
    cliente_cantidad = int(input("¿Cuántas unidades deseas comprar hoy?: "))
    
    print("Procesando el pago...")
    
    # 4. Lógica de cálculo directo
    if cliente_cantidad >= 5:
        costo_envio = 0
    else:
        costo_envio = 4500
        
    total = (25000 * cliente_cantidad) + costo_envio
    
    # 5. Generamos el recibo para este cliente
    print("\n--- 🧾 RECIBO DE COMPRA ---")
    print(f"✅ ¡Gracias por tu compra, {cliente_nombre}!")
    print(f"📍 Despacharemos tu producto a: {cliente_direccion}")
    print(f"💰 Total cargado: ${total}")
    print("---------------------------\n")
    
    # Al llegar aquí, el ciclo vuelve automáticamente arriba a esperar al siguiente cliente