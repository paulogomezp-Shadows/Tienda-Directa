import flet as ft
import requests 
import json
import os

def main(page: ft.Page):
    page.title = "Tienda Directa - Venta de Producto"
    page.window_width = 360 
    page.window_height = 740
    page.horizontal_alignment = "center" 
    
    titulo = ft.Text("¡Bienvenido a la Tienda!", size=28, weight="bold", color="blue")
    
    archivo_memoria = "memoria_app.json"
    nombre_guardado = ""
    direccion_guardada = ""
    
    if os.path.exists(archivo_memoria):
        with open(archivo_memoria, "r", encoding="utf-8") as f:
            datos_guardados = json.load(f)
            nombre_guardado = datos_guardados.get("nombre", "")
            direccion_guardada = datos_guardados.get("direccion", "")
    
    campo_nombre = ft.TextField(label="Tu Nombre", value=nombre_guardado, width=300)
    campo_direccion = ft.TextField(label="Dirección de Envío", value=direccion_guardada, width=300)
    campo_cupon = ft.TextField(label="Cupón de Descuento (Opcional)", width=300)
    
    campo_cantidad = ft.TextField(value="1", width=60, text_align="center", read_only=True)
    
    def disminuir(e):
        valor_actual = int(campo_cantidad.value)
        if valor_actual > 1:
            campo_cantidad.value = str(valor_actual - 1)
            page.update()

    def aumentar(e):
        valor_actual = int(campo_cantidad.value)
        campo_cantidad.value = str(valor_actual + 1)
        page.update()

    boton_menos = ft.ElevatedButton("-", on_click=disminuir, bgcolor="red", color="white", width=50)
    boton_mas = ft.ElevatedButton("+", on_click=aumentar, bgcolor="green", color="white", width=50)
    
    selector_cantidad = ft.Row(
        [ft.Text("Cantidad:", size=16), boton_menos, campo_cantidad, boton_mas],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # --- NUEVO COMPONENTE: Selector de Pago ---
    opciones_pago = ft.Dropdown(
        label="Método de Pago",
        width=300,
        options=[
            ft.dropdown.Option("Transferencia Directa"),
            ft.dropdown.Option("Tarjeta de Crédito")
        ],
        value="Transferencia Directa" # Dejamos la transferencia como opción por defecto
    )
    # ------------------------------------------

    mensaje_estado = ft.Text("", size=16, weight="bold")

    def procesar_compra(evento):
        mensaje_estado.value = "Procesando orden..."
        mensaje_estado.color = "blue"
        page.update() 
        
        try:
            # Actualizamos el paquete para que viaje con el método de pago a la nube
            paquete = {
                "cliente": campo_nombre.value,
                "direccion": campo_direccion.value,
                "pedido": {
                    "cantidad": int(campo_cantidad.value)
                },
                "cupon": campo_cupon.value,
                "metodo_pago": opciones_pago.value
            }
            
            respuesta = requests.post("https://PgomezP.pythonanywhere.com/comprar", json=paquete)
            
            if respuesta.status_code == 200:
                datos_servidor = respuesta.json()
                mensaje_estado.value = f"¡Éxito! Folio: {datos_servidor['folio']} \nTotal: ${datos_servidor['total_cobrado']}"
                mensaje_estado.color = "green"
                
                with open(archivo_memoria, "w", encoding="utf-8") as f:
                    json.dump({
                        "nombre": campo_nombre.value, 
                        "direccion": campo_direccion.value
                    }, f)
                
            else:
                mensaje_estado.value = f"Rechazado: Error {respuesta.status_code}"
                mensaje_estado.color = "red"
                
        except Exception as e:
            mensaje_estado.value = "Error de red. Verifica tu conexión."
            mensaje_estado.color = "red"
            
        page.update() 

    boton_comprar = ft.ElevatedButton("Confirmar Compra", width=300, on_click=procesar_compra)
    
    page.add(
        titulo,
        campo_nombre,
        campo_direccion,
        campo_cupon,
        selector_cantidad,
        opciones_pago, # Agregamos el menú a la pantalla
        boton_comprar,
        mensaje_estado
    )

if __name__ == "__main__":
    ft.app(target=main)