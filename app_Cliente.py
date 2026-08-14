import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Tienda Directa"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F4F6F9"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # --- 1. MEMORIA Y PRECIOS ---
    cantidad_actual = 1
    precio_unitario = 25000

    # --- 2. LA INTERFAZ VISUAL ---
    imagen_producto = ft.Image(
        src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?q=80&w=400&auto=format&fit=crop", 
        width=300, height=300, fit="contain"
    )
    titulo = ft.Text("Aceite de Oliva Premium", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    subtitulo = ft.Text("¡Bienvenido a la Tienda!", size=18, color=ft.Colors.BLUE_GREY_700)

    txt_nombre = ft.TextField(label="Tu Nombre", border_radius=10)
    txt_direccion = ft.TextField(label="Dirección de Envío", border_radius=10)
    txt_cupon = ft.TextField(label="Cupón de Descuento (Opcional)", border_radius=10)

    # Elementos dinámicos que van a cambiar en pantalla
    lbl_cantidad = ft.Text(str(cantidad_actual), size=20, weight=ft.FontWeight.BOLD)
    lbl_total = ft.Text(f"Total a Pagar: ${precio_unitario}", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lbl_resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)

    # --- 3. EL MOTOR (LAS FUNCIONES) ---
    def sumar_cantidad(e):
        nonlocal cantidad_actual
        cantidad_actual += 1
        lbl_cantidad.value = str(cantidad_actual)
        lbl_total.value = f"Total a Pagar: ${cantidad_actual * precio_unitario}"
        page.update() # Refresca la pantalla

    def restar_cantidad(e):
        nonlocal cantidad_actual
        if cantidad_actual > 1:
            cantidad_actual -= 1
            lbl_cantidad.value = str(cantidad_actual)
            lbl_total.value = f"Total a Pagar: ${cantidad_actual * precio_unitario}"
            page.update() # Refresca la pantalla

    def procesar_compra(e):
        # 1. Bloquear botón mientras procesa
        btn_confirmar.disabled = True
        btn_confirmar.text = "Enviando pedido..."
        lbl_resultado.value = ""
        page.update()

        # 2. Empaquetar los datos
        datos_pedido = {
            "nombre": txt_nombre.value,
            "direccion": txt_direccion.value,
            "cupon": txt_cupon.value,
            "cantidad": cantidad_actual,
            "metodo_pago": dropdown_pago.value,
            "total": cantidad_actual * precio_unitario
        }

        # 3. Enviar al servidor 
        try:
            # NOTA: Cambia esta URL por la real de tu servidor web
            url_servidor = "https://tu-servidor-web.com/api/nuevo_pedido"
            
            # Simulamos el éxito para que puedas probar la interfaz ya mismo
            import time
            time.sleep(1.5) # Simula el tiempo de carga de internet
            
            lbl_resultado.value = "¡Éxito! Folio: 84653"
            lbl_resultado.color = ft.Colors.GREEN_600
        except Exception as ex:
            lbl_resultado.value = "Error de conexión."
            lbl_resultado.color = ft.Colors.RED_600

        # 4. Restaurar botón
        btn_confirmar.disabled = False
        btn_confirmar.text = "Confirmar Compra"
        page.update()

    # --- 4. CONECTANDO LOS CABLES A LOS BOTONES ---
    btn_menos = ft.IconButton(icon=ft.Icons.REMOVE, bgcolor=ft.Colors.RED_400, icon_color=ft.Colors.WHITE, on_click=restar_cantidad)
    btn_mas = ft.IconButton(icon=ft.Icons.ADD, bgcolor=ft.Colors.GREEN_600, icon_color=ft.Colors.WHITE, on_click=sumar_cantidad)
    
    fila_cantidad = ft.Row(
        controls=[ft.Text("Cantidad:", size=16), btn_menos, lbl_cantidad, btn_mas],
        alignment=ft.MainAxisAlignment.CENTER
    )

    dropdown_pago = ft.Dropdown(
        label="Método de Pago",
        options=[ft.dropdown.Option("Tarjeta de Crédito"), ft.dropdown.Option("Transferencia")],
        border_radius=10,
        value="Tarjeta de Crédito"
    )
    
    btn_confirmar = ft.ElevatedButton(
        "Confirmar Compra",
        icon="shopping_cart_checkout",
        style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_900),
        width=300, height=50,
        on_click=procesar_compra # <--- AQUÍ SE CONECTA LA ACCIÓN DE COMPRAR
    )

    # --- 5. EMPAQUETAR LA TARJETA ---
    formulario = ft.Container(
        content=ft.Column([
            txt_nombre, txt_direccion, txt_cupon,
            ft.Divider(),
            fila_cantidad,
            lbl_total,
            ft.Divider(),
            dropdown_pago,
            btn_confirmar,
            lbl_resultado # Etiqueta oculta que mostrará el mensaje de éxito
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.Colors.WHITE, padding=20, border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12)
    )

    page.add(imagen_producto, titulo, subtitulo, formulario)

ft.app(target=main)
