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
    titulo = ft.Text("Aceite de Oliva Premium", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    subtitulo = ft.Text("¡Bienvenido a la Tienda!", size=18, color=ft.Colors.BLUE_GREY_700)

    # 3. Campos de Entrada (ahora con iconos como texto en minúsculas)
    txt_nombre = ft.TextField(label="Tu Nombre", prefix_icon="person_outline", border_radius=10)
    txt_direccion = ft.TextField(label="Dirección de Envío", prefix_icon="location_on_outlined", border_radius=10)
    txt_cupon = ft.TextField(label="Cupón de Descuento", prefix_icon="local_offer_outlined", border_radius=10)

    # 4. Controles de cantidad (Botones circulares con iconos en texto)
    lbl_cantidad = ft.Text("1", size=20, weight=ft.FontWeight.BOLD)
    btn_menos = ft.IconButton(icon="remove", bgcolor=ft.Colors.RED_400, icon_color=ft.Colors.WHITE)
    btn_mas = ft.IconButton(icon="add", bgcolor=ft.Colors.GREEN_600, icon_color=ft.Colors.WHITE)
    
    fila_cantidad = ft.Row(
        controls=[ft.Text("Cantidad:", size=16), btn_menos, lbl_cantidad, btn_mas],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # 5. Método de pago y Botón principal
    dropdown_pago = ft.Dropdown(
        label="Método de Pago",
        options=[ft.dropdown.Option("Tarjeta de Crédito"), ft.dropdown.Option("Transferencia")],
        border_radius=10
    )
    
    btn_confirmar = ft.ElevatedButton(
        text="Confirmar Compra",
        icon="shopping_cart_checkout",
        bgcolor=ft.Colors.BLUE_900,
        color=ft.Colors.WHITE,
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
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12)
    )

    # Agregar todo a la pantalla
    page.add(
        imagen_producto,
        titulo,
        subtitulo,
        formulario
    )

ft.app(target=main)
