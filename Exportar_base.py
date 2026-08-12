# 1. Tu base de datos (lo que tu app recopiló durante el día)
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

print("Procesando la base de datos de la aplicación...")

# 2. Creamos el archivo final para la empresa de envíos
with open("nomina_despachos.csv", "w", encoding="utf-8") as archivo:
    
    # Escribimos los encabezados de las columnas
    archivo.write("Nombre_Cliente,Direccion_Exacta,Unidades_Compradas\n")
    
    # 3. El bucle recorre la lista maestra
    for cliente in pedidos_app:
        
        # Extraemos los datos del diccionario a variables simples para mayor claridad
        nombre = cliente["nombre"]
        direccion = cliente["direccion_envio"]
        cantidad = cliente["unidades"]
        
        # 4. Escribimos la fila en el CSV, separando los datos estrictamente por comas
        archivo.write(f'{nombre},"{direccion}",{cantidad}\n')

print("¡Éxito! El archivo 'nomina_despachos.csv' está listo para ser enviado.")