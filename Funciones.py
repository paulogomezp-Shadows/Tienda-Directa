print("🛠️ Motor de Reglas de Negocio (Versión Promocional) Iniciado 🛠️\n")

def calcular_costo_envio(cantidad):
    if cantidad >= 5:
        return 0
    else:
        return 4500

# Agregamos el cupón como un parámetro nuevo. 
# Le ponemos ="" para que, si el cliente no tiene cupón, el sistema no colapse.
def calcular_total_pagar(cantidad, precio_unitario, cupon=""):
    envio = calcular_costo_envio(cantidad)
    subtotal = cantidad * precio_unitario
    descuento = 0
    
    # Lógica del código de descuento
    # Usamos .upper() por si el cliente lo escribe en minúsculas
    if cupon.upper() == "VIP2026":
        # 15% de descuento sobre el valor de los productos (0.15)
        descuento = subtotal * 0.15 
        
    total_final = (subtotal - descuento) + envio
    
    # Opcional: devolvemos un número entero sin decimales
    return int(total_final)

# --- ZONA DE PRUEBAS ---
print("Simulando compras para la App Móvil...\n")

compra_normal = calcular_total_pagar(2, 25000)

# A esta compra le pasamos exactamente los mismos datos, pero agregamos el código secreto
compra_con_descuento = calcular_total_pagar(2, 25000, "VIP2026")

print("--- 🧾 RESULTADOS AUTOMÁTICOS ---")
print(f"Compra normal (2 unidades): ${compra_normal}")
print(f"Compra VIP (2 unidades, código VIP2026): ${compra_con_descuento}")
print("---------------------------------")