Precio_Producto = 25000
Costo_envio = 4500
Pedidos_del_Dia = [1, 5, 3, 10, 2, 8, 4]
for Pedidos in Pedidos_del_Dia:
    if Pedidos >= 5:
        Costo_Envio_Final = 0
    else:
        Costo_Envio_Final = Costo_envio

    Subtotal = Precio_Producto * Pedidos
    Total = Subtotal + Costo_Envio_Final

    print("\n--- RESUMEN POR PEDIDO ---")
    print("Unidades:", Pedidos)
    print("Total Productos: $", Subtotal)
    print("Total Envio: $", Costo_Envio_Final)
    print("Total final a cobrar: $", Total)