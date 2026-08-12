precio_producto = 25000
costo_envio_base = 4500
pedidos_del_dia = [1, 5, 3, 10, 2, 8, 4]

print("Generando base de datos para logística...")

# Cambiamos la extensión a .csv
with open("despachos_diarios.csv", "w", encoding="utf-8") as archivo:
    
    # 1. Escribimos la primera fila: Los encabezados de las columnas
    archivo.write("Unidades_Compradas,Subtotal,Costo_Envio,Total_Cobrado\n")
    
    # 2. Procesamos las ventas
    for cantidad in pedidos_del_dia:
        if cantidad >= 5:
            envio_final = 0
        else:
            envio_final = costo_envio_base
            
        subtotal = precio_producto * cantidad
        total = subtotal + envio_final
        
        # 3. Escribimos los datos matemáticos separados por comas
        archivo.write(f"{cantidad},{subtotal},{envio_final},{total}\n")

print("¡Archivo 'despachos_diarios.csv' generado con éxito!")