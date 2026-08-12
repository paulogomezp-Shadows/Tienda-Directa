print("Conectando con la base de datos de usuarios...\n")

# 1. Creamos el diccionario del comprador
usuario_app = {
    "nombre": "Paulo",
    "telefono": "+56912345678",
    "direccion_envio": "Av. Los Cóndores 456, Depto 12",
    "unidades_compradas": 2
}

# 2. Extraemos los datos usando sus llaves para generar la etiqueta
print("--- ETIQUETA DE DESPACHO ---")

# ¡Ojo al detalle! En los f-strings, si usas comillas dobles "" por fuera, 
# debes usar comillas simples '' adentro de las llaves para llamar al diccionario.
print(f"Destinatario: {usuario_app['nombre']}")
print(f"Ruta de entrega: {usuario_app['direccion_envio']}")
print(f"Contacto: {usuario_app['telefono']}")
print("----------------------------")