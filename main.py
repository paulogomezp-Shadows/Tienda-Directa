import flet as ft
import requests

# === 🌐 CONFIGURACIÓN DE RED (LA CONEXIÓN A TU NUBE) ===
# Reemplaza 'tuusuario' por tu cuenta real de PythonAnywhere
URL_SERVIDOR = "https://PgomezP.pythonanywhere.com"

def main(page: ft.Page):
    page.title = "Tienda Directa"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F4F6F9"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # --- 1. MEMORIA ---
    cantidad_actual = 1

    # --- 2. LA INTERFAZ VISUAL ---
    imagen_producto = ft.Image(
        src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?q=80&w=400&auto=format&fit=crop", 
        width=300, height=300, fit="contain"
    )
    titulo = ft.Text("Aceite de Oliva Premium", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    subtitulo = ft.Text("¡Bienvenido a la Tienda!", size=18, color=ft.Colors.BLUE_GREY_700)

    txt_nombre = ft.TextField(label="Tu Nombre", border_radius=10)
    txt_direccion = ft.TextField(label="Dirección de Envío", border_radius=10)
    
    lbl_cantidad = ft.Text(str(cantidad_actual), size=20, weight=ft.FontWeight.BOLD)
    lbl_desglose = ft.Text("Conectando al servidor...", size=14, color=ft.Colors.BLUE_GREY_500)
    lbl_total = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lbl_resultado = ft.Text("", size=16, weight=ft.FontWeight.BOLD)

    # --- 3. CONEXIÓN A LA VENTANILLA DE COTIZACIONES ---
    def calcular_totales(e=None):
        lbl_total.value = "Calculando..."
        page.update()

        try:
            respuesta = requests.post(f"{URL_SERVIDOR}/api/calcular_totales", json={
                "cantidad": cantidad_actual,
                "cupon": txt_cupon.value
            }, timeout=5)
            
            if respuesta.status_code == 200:
                datos_servidor = respuesta.json()
                lbl_desglose.value = f"Subtotal: ${datos_servidor['subtotal']} | Envío: ${datos_servidor['envio']} | Dcto: -${datos_servidor['descuento']}"
                lbl_total.value = f"Total a Pagar: ${datos_servidor['total_final']}"
            else:
                lbl_total.value = "Error en el cálculo."
                
        except requests.exceptions.RequestException:
            lbl_total.value = "Error de conexión."
            lbl_desglose.value = f"No se pudo contactar a tu servidor en la nube."
            
        page.update()

    txt_cupon = ft.TextField(
        label="Cupón de Descuento", 
        border_radius=10, 
        on_change=calcular_totales 
    )

    def sumar_cantidad(e):
        nonlocal cantidad_actual
        cantidad_actual += 1
        lbl_cantidad.value = str(cantidad_actual)
        calcular_totales()

    def restar_cantidad(e):
        nonlocal cantidad_actual
        if cantidad_actual > 1:
            cantidad_actual -= 1
            lbl_cantidad.value = str(cantidad_actual)
            calcular_totales()

    # --- 4. CONEXIÓN A LA CAJA REGISTRADORA ---
    def procesar_compra(e):
        nonlocal cantidad_actual # <--- ¡EL SALVAVIDAS MOVIDO AL PRINCIPIO!
        
        btn_confirmar.disabled = True
        btn_confirmar.text = "Procesando..."
        lbl_resultado.value = ""
        page.update()
        
        try:
            payload = {
                "cliente": txt_nombre.value,
                "direccion": txt_direccion.value,
                "pedido": {"cantidad": cantidad_actual},
                "cupon": txt_cupon.value,
                "metodo_pago": dropdown_pago.value
            }
            
            respuesta = requests.post(f"{URL_SERVIDOR}/comprar", json=payload, timeout=5)
            datos_respuesta = respuesta.json()
            
            if respuesta.status_code == 200:
                lbl_resultado.value = f"¡Éxito! Folio: {datos_respuesta.get('folio', '')}"
                lbl_resultado.color = ft.Colors.GREEN_600
                
                txt_nombre.value = ""
                txt_direccion.value = ""
                txt_cupon.value = ""
                
                # Reiniciamos la memoria sin romper Python
                cantidad_actual = 1
                lbl_cantidad.value = "1"
                calcular_totales()
            else:
                lbl_resultado.value = datos_respuesta.get("mensaje", "Error en la orden.")
                lbl_resultado.color = ft.Colors.RED_600
                
        except requests.exceptions.RequestException:
            lbl_resultado.value = "Error de red. Revisa tu conexión a internet."
            lbl_resultado.color = ft.Colors.RED_600
            
        btn_confirmar.disabled = False
        btn_confirmar.text = "Confirmar Compra"
        page.update()

    # --- 5. EMPAQUETADO VISUAL ---
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
        on_click=procesar_compra
    )

    formulario = ft.Container(
        content=ft.Column([
            txt_nombre, txt_direccion, txt_cupon,
            ft.Divider(),
            fila_cantidad,
            lbl_desglose, 
            lbl_total,
            ft.Divider(),
            dropdown_pago,
            btn_confirmar,
            lbl_resultado
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.Colors.WHITE, padding=20, border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12)
    )

    page.add(imagen_producto, titulo, subtitulo, formulario)
    
    calcular_totales()

ft.app(target=main)