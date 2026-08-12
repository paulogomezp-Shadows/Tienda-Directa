import Funciones
import random  # 1. Importamos la herramienta para crear números aleatorios

print("🛡️ Servidor Central (Versión Producción) Iniciado 🛡️\n")

while True:
    print("\n--- NUEVA COMPRA ---")
    cliente_nombre = input("Ingresa tu nombre (o 'salir' para apagar): ")
    
    if cliente_nombre.lower() == "salir":
        print("Apagando el servidor central... ¡Buenas noches!")
        break
        
    cliente_direccion = input("Ingresa tu dirección exacta para el envío: ")
    cantidad_texto = input("¿Cuántas unidades deseas comprar hoy?: ")
    cupon_texto = input("¿Tienes un código de descuento? (Presiona Enter si no tienes): ")
    
    try:
        cliente_cantidad = int(cantidad_texto)
        total = Funciones.calcular_total_pagar(cliente_cantidad, 25000, cupon_texto)
        
        # 2. Generamos un número de pedido único (entre 10000 y 99999)
        folio_pedido = random.randint(10000, 99999)
        
        print("\n--- 🧾 RECIBO DE COMPRA ---")
        # 3. Le mostramos el número de seguimiento al cliente
        print(f"📌 Folio de Pedido: #{folio_pedido}")
        print(f"✅ ¡Gracias por tu compra, {cliente_nombre}!")
        
        if cupon_texto.upper() == "VIP2026":
            print("✨ ¡Cupón VIP del 15% aplicado exitosamente!")
            
        print(f"💰 Total a pagar: ${total}")
        
        # 4. Guardamos el folio en nuestra base de datos para que el transportista lo vea
        with open("nomina_despachos.csv", "a", encoding="utf-8") as archivo:
            # Agregamos el folio al principio de la línea
            archivo.write(f'{folio_pedido},{cliente_nombre},"{cliente_direccion}",{cliente_cantidad}\n')
            
        print("💾 Pedido guardado exitosamente en la base logística con su folio.")
        print("---------------------------\n")
        
    except ValueError:
        print("⚠️ ERROR: Por favor, ingresa la cantidad usando solo números (ej: 2, 4, 10).")