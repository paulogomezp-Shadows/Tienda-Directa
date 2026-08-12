import json

print("📡 Servidor escuchando a la App Móvil...\n")

# 1. Esto es lo que la app móvil envía cuando el cliente presiona "Comprar"
# Es un Diccionario de Python estructurado
datos_compra = {
    "cliente": "Paulo Silva",
    "direccion": "Juan Retamal 735",
    "pedido": {
        "producto": "Producto Estrella",
        "cantidad": 8,
        "envio_gratis": True
    },
    "total_pagado": 200000
}

# 2. Convertimos el diccionario a texto JSON (el idioma de internet)
# El 'indent=4' es solo para que se imprima bonito y ordenado en pantalla
paquete_json = json.dumps(datos_compra, indent=4)

print("📦 Paquete JSON recibido:")
print(paquete_json)

# 3. Guardamos este paquete como un archivo .json formal
with open("ultimo_pedido.json", "w", encoding="utf-8") as archivo:
    # json.dump guarda directamente el diccionario en el archivo físico
    json.dump(datos_compra, archivo, indent=4)
    
print("\n💾 Archivo 'ultimo_pedido.json' generado con éxito en el servidor.")