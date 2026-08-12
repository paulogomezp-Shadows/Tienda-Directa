print("Sincronizando compras de la aplicación...\n")

# 1. Creamos la Lista Maestra que contiene los Diccionarios
pedidos_app = [
    {
        "nombre": "Paulo",
        "direccion_envio": "Av. Los Cóndores 456, Depto 12",
        "unidades": 2
    },
    {
        "nombre": "Ana",
        "direccion_envio": "Calle Las Rosas 89",
        "unidades": 5
    },
    {
        "nombre": "Carlos",
        "direccion_envio": "Av. Libertador 1024, Casa 3",
        "unidades": 1
    }
]

print("--- GENERANDO ETIQUETAS DE ENVÍO MASIVAS ---\n")

# 2. El bucle FOR recorre la lista. 
# En cada vuelta, la variable 'cliente' se convierte en un diccionario completo.
for cliente in pedidos_app:
    print(f"📦 Preparando envío para: {cliente['nombre']}")
    print(f"📍 Destino: {cliente['direccion_envio']}")
    print(f"🛍️ Unidades a despachar: {cliente['unidades']}")
    print("-" * 40)