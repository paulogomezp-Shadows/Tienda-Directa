print("Abriendo base de datos logística...\n")

# Creamos una variable en cero para ir sumando el dinero
ingreso_total = 0

# Ahora abrimos el archivo en modo lectura ("r" de read)
with open("despachos_diarios.csv", "r", encoding="utf-8") as archivo:
    
    # archivo.readlines() toma todas las filas y las guarda en una lista
    filas = archivo.readlines()
    
    # Hacemos un bucle FOR pero omitimos la primera fila (los encabezados) 
    # usando [1:] que significa "empieza desde la posición 1 en adelante"
    for fila in filas[1:]:
        
        # 1. Limpiamos espacios/saltos de línea con strip() y separamos por comas con split()
        columnas = fila.strip().split(",")
        
        # 2. Extraemos el último dato (el Total_Cobrado). 
        # En programación, la posición 0 es la primera, por ende la 3 es la cuarta columna.
        total_texto = columnas[3]
        
        # 3. Convertimos ese texto a un número entero (int) para poder sumarlo
        total_numero = int(total_texto)
        
        # 4. Lo sumamos a nuestro acumulador
        ingreso_total = ingreso_total + total_numero

print(f"💰 El ingreso total del día calculado desde el archivo CSV es: ${ingreso_total}")