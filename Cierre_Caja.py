import datetime
import csv  # 1. Importamos el lector profesional de bases de datos planas

print("📊 Generando Reporte de Cierre de Caja (Versión Blindada) 📊\n")

momento_actual = datetime.datetime.now()
fecha_bonita = momento_actual.strftime("%d/%m/%Y %H:%M")

total_unidades_vendidas = 0
precio_producto = 25000

# 2. Leemos la base de datos logística usando el motor csv
with open("nomina_despachos.csv", "r", encoding="utf-8") as archivo:
    # Este lector entiende que si hay comas dentro de comillas (como en una dirección), 
    # no debe separarlas.
    lector_csv = csv.reader(archivo)
    
    # Saltamos la primera línea (los encabezados) de forma elegante
    next(lector_csv, None)
    
    for fila in lector_csv:
        # Si encuentra una fila en blanco por error, la salta para no romperse
        if not fila:
            continue
            
        # Como el lector_csv ya organizó la fila perfectamente, 
        # sabemos que el último dato [-1] es 100% seguro la cantidad.
        cantidad_comprada = int(fila[-1])
        total_unidades_vendidas += cantidad_comprada

ingresos_totales = total_unidades_vendidas * precio_producto

# 3. Inyectamos la variable "fecha_bonita" en el encabezado
texto_resumen = (
    f"--- 📈 RESUMEN DEL DÍA: {fecha_bonita} ---\n"
    f"📦 Total de productos a despachar: {total_unidades_vendidas} unidades\n"
    f"💰 Ingresos brutos generados: ${ingresos_totales}\n"
    "------------------------------------------------\n"
)

print(texto_resumen)

# Exportamos el reporte auditable
with open("resumen_diario.txt", "w", encoding="utf-8") as reporte:
    reporte.write("REPORTE OFICIAL DE VENTAS Y LOGÍSTICA\n")
    reporte.write("=====================================\n\n")
    reporte.write(texto_resumen)
    
print("💾 ¡El archivo 'resumen_diario.txt' ha sido actualizado con éxito!")