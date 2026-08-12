import requests

print("📱 Simulador de App Móvil Iniciado")
print("Preparando paquete de datos...")

# 1. La dirección exacta de tu puerta de ventas
url = "http://127.0.0.1:5000/comprar"

# 2. El paquete de datos JSON que enviaría el celular
datos_venta = {
    "cliente": "Paulo",
    "direccion": "Avenida Las Condes 1234, Depto 45",
    "pedido": {
        "cantidad": 3
    },
    "cupon": "VIP2026"
}

print("Enviando orden de compra al servidor central por internet...\n")

# 3. ¡El disparo! Hacemos la petición POST enviando el JSON
respuesta = requests.post(url, json=datos_venta)

# 4. Leemos lo que el servidor nos devolvió
print("--- 📩 RESPUESTA DEL SERVIDOR ---")
print(respuesta.json())
print("---------------------------------")