import json
import random
import Funciones

print("🚀 SISTEMA DE VENTAS AUTOMATIZADO INICIADO 🚀\n")
print("Buscando nuevas órdenes desde la App Móvil...\n")

try:
    # 1. Leemos el paquete JSON que envió la aplicación
    with open("ultimo_pedido.json", "r", encoding="utf-8") as archivo:
        datos_app = json.load(archivo)
        
    print("📥 ¡Nuevo pedido recibido desde la App!")
    
    # 2. Extraemos los datos del diccionario JSON
    cliente = datos_app["cliente"]
    direccion = datos_app["direccion"]
    cantidad = datos_app["pedido"]["cantidad"]
    
    # Simulamos que la app también podría enviar un cupón (o un texto vacío si no hay)
    cupon = "VIP2026" 
    
    # 3. Procesamos la matemática usando tu Motor de Reglas
    total_a_cobrar = Funciones.calcular_total_pagar(cantidad, 25000, cupon)
    folio = random.randint(10000, 99999)
    
    # 4. Guardamos directamente en la base logística
    with open("nomina_despachos.csv", "a", encoding="utf-8") as bd:
        bd.write(f'{folio},{cliente},"{direccion}",{cantidad}\n')
        
    # 5. Imprimimos el resultado de la operación invisible
    print("--- ⚙️ PROCESAMIENTO EXITOSO ⚙️ ---")
    print(f"📌 Folio asignado: #{folio}")
    print(f"👤 Cliente: {cliente}")
    print(f"💰 Total calculado por el motor: ${total_a_cobrar}")
    print("💾 Registro inyectado en nomina_despachos.csv")
    print("-----------------------------------\n")

except FileNotFoundError:
    print("⚠️ No hay pedidos nuevos en la bandeja de entrada.")