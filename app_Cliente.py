import flet as ft

def main(page: ft.Page):
    page.title = "Tienda Directa"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F4F6F9" # Fondo sutil
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # 1. La imagen del producto (Vitrina)
    imagen_producto = ft.Image(
        src="https://picsum.photos/400/400", # Reemplaza con el link a la foto real de tu producto
        width=300,
        height=300,
        fit="contain",
    )

    # 2. Textos de Bienvenida
    titulo = ft.Text("Aceite de Oliva Premium", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900)
    subtitulo = ft.Text("¡Bienvenido a la Tienda!", size=18, color=ft.colors.BLUE_GREY_700)

    # 3. Campos de Entrada (ahora con iconos)
    txt_nombre = ft.TextField(label="Tu Nombre", prefix_icon=ft.icons.PERSON_OUTLINE, border_radius=10)
    txt_direccion = ft.TextField(label="Dirección de Envío", prefix_icon=ft.icons.LOCATION_ON_OUTLINED, border_radius=10)
    txt_cupon = ft.TextField(label="Cupón de Descuento", prefix_icon=ft.icons.LOCAL_OFFER_OUTLINED, border_radius=10)

    # 4. Controles de cantidad (Botones circulares)
    lbl_cantidad = ft.Text("1", size=20, weight=ft.FontWeight.BOLD)
    btn_menos = ft.IconButton(icon=ft.icons.REMOVE, bgcolor=ft.colors.RED_400, icon_color=ft.colors.WHITE)
    btn_mas = ft.IconButton(icon=ft.icons.ADD, bgcolor=ft.colors.GREEN_600, icon_color=ft.colors.WHITE)
    
    fila_cantidad = ft.Row(
        controls=[ft.Text("Cantidad:", size=16), btn_menos, lbl_cantidad, btn_mas],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # 5. Método de pago y Botón principal
    dropdown_pago = ft.Dropdown(
        label="Método de Pago",
        prefix_icon=ft.icons.CREDIT_CARD,
        options=[ft.dropdown.Option("Tarjeta de Crédito"), ft.dropdown.Option("Transferencia")],
        border_radius=10
    )
    
    btn_confirmar = ft.ElevatedButton(
        text="Confirmar Compra",
        icon=ft.icons.SHOPPING_CART_CHECKOUT,
        bgcolor=ft.colors.BLUE_900,
        color=ft.colors.WHITE,
        width=300,
        height=50
    )

    # 6. Empaquetar todo en una Tarjeta Blanca (Card)
    formulario = ft.Container(
        content=ft.Column([
            txt_nombre,
            txt_direccion,
            txt_cupon,
            ft.Divider(),
            fila_cantidad,
            ft.Divider(),
            dropdown_pago,
            btn_confirmar
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.BLACK12)
    )

    # Agregar todo a la pantalla
    page.add(
        imagen_producto,
        titulo,
        subtitulo,
        formulario
    )

ft.app(target=main)