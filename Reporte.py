print("Iniciando el sistema de exportación...")

# Usamos 'with open' para abrir el archivo en modo escritura ('w')
# Python se encargará de cerrarlo automáticamente cuando termine.
with open("resumen_diario.txt", "w", encoding="utf-8") as archivo:
    archivo.write("--- REPORTE AUTOMÁTICO DE VENTAS ---\n")
    archivo.write("Pedido 1: 5 unidades - Envio Gratis\n")
    archivo.write("Pedido 2: 2 unidades - Envio $4500\n")
    archivo.write("Estado: Procesado con éxito.")

print("¡El archivo ha sido creado y guardado en tu carpeta!")