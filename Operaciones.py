# 1. Datos iniciales
precio_unico_producto = 25000
costo_envio_base = 4500.50

print("--- BIENVENIDO A LA TIENDA ---")
nombre_cliente = input("Por favor, ingresa tu nombre: ")
cantidad_comprada = int(input("¿Cuántas unidades deseas comprar?: "))

# 2. LA TOMA DE DECISIONES (if / else)
if cantidad_comprada >= 5:
    # Si compra 5 o más, el costo de envío se vuelve cero
    costo_envio_final = 0
    print("\n¡Felicidades", nombre_cliente, "! Tienes ENVÍO GRATIS por comprar 5 o más unidades.")
else:
    # De lo contrario, se cobra la tarifa normal
    costo_envio_final = costo_envio_base
    print("\nEl envío tendrá un costo de $", costo_envio_final)

# 3. Matemáticas finales usando el costo de envío que se decidió arriba
subtotal = precio_unico_producto * cantidad_comprada
total_a_pagar = subtotal + costo_envio_final

# 4. Resumen
print("\n--- RESUMEN DEL PEDIDO ---")
print("Unidades:", cantidad_comprada)
print("Subtotal: $", subtotal)
print("Total final a cobrar: $", total_a_pagar)