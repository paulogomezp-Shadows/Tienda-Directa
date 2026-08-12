import json

print("🚚 Sistema de Logística - Generando Etiqueta 🚚\n")

# 1. Abrimos el archivo JSON en modo lectura ("r")
with open("ultimo_pedido.json", "r", encoding="utf-8") as archivo:
    # json.load hace la magia inversa: convierte el archivo web de vuelta a un Diccionario de Python
    pedido_recuperado = json.load(archivo)

# 2. Navegamos por el diccionario pidiendo exactamente lo que queremos
nombre_cliente = pedido_recuperado["cliente"]
direccion_envio = pedido_recuperado["direccion"]

# Para llegar a un dato "anidado" (dentro de otro bloque), simplemente encadenamos las llaves
producto_comprado = pedido_recuperado["pedido"]["producto"]
cantidad = pedido_recuperado["pedido"]["cantidad"]

# 3. Imprimimos la etiqueta limpia para el transportista
print("--- 🏷️ ETIQUETA DE DESPACHO ---")
print(f"👤 Destinatario: {nombre_cliente}")
print(f"📍 Entregar en: {direccion_envio}")
print(f"📦 Contenido: {cantidad}x {producto_comprado}")
print("-------------------------------\n")