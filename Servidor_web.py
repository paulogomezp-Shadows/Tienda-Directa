from flask import Flask, jsonify, request
import random
import Funciones
import csv
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime # <-- NUEVO 1: Herramienta para guardar la fecha y hora de la compra

# --- CONFIGURACIÓN DE LA BASE DE DATOS GOOGLE SHEETS ---
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
try:
    credenciales = Credentials.from_service_account_file("credenciales.json", scopes=SCOPES)
    cliente_gspread = gspread.authorize(credenciales)
    hoja_bd = cliente_gspread.open("Pedidos_Aceite_Premium").sheet1
except Exception as e:
    print(f"Error al conectar con Google Sheets: {e}")
    hoja_bd = None

app = Flask(__name__)

# --- ⚙️ TU PANEL DE CONTROL (Modifica esto sin tocar la app) ---
PRECIO_UNITARIO = 25000
COSTO_ENVIO_BASE = 5000
CANTIDAD_ENVIO_GRATIS = 5
CUPON_ACTIVO = "vip2006"
DESCUENTO_CUPON = 0.10 # 10%
# --------------------------------------------------------------

# --- 🧠 NUEVA RUTA: EL CEREBRO DE CÁLCULO ---
@app.route('/api/calcular_totales', methods=['POST'])
def calcular_totales():
    # 1. Recibir los datos que manda la aplicación
    datos_cliente = request.get_json()
    cantidad = datos_cliente.get('cantidad', 1)
    cupon = datos_cliente.get('cupon', '').strip().lower()

    # 2. Hacer las matemáticas
    subtotal = cantidad * PRECIO_UNITARIO
    envio = 0 if cantidad >= CANTIDAD_ENVIO_GRATIS else COSTO_ENVIO_BASE
    
    descuento = 0
    if cupon == CUPON_ACTIVO:
        descuento = int(subtotal * DESCUENTO_CUPON)

    total_final = subtotal + envio - descuento

    # 3. Devolver los resultados a la aplicación
    return jsonify({
        "subtotal": subtotal,
        "envio": envio,
        "descuento": descuento,
        "total_final": total_final
    })
# --------------------------------------------

@app.route('/estado', methods=['GET'])
def verificar_conexion():
    return jsonify({"estado": "En línea", "mensaje": "Servidor central operativo."})

@app.route('/comprar', methods=['POST'])
def procesar_venta():
    # 1. Envolvemos toda la operación en un campo de fuerza
    try:
        datos_app = request.get_json()
        
        cliente = datos_app["cliente"]
        direccion = datos_app["direccion"]
        
        # Si la app envía texto en vez de número, esto fallará y saltará al 'except'
        cantidad = int(datos_app["pedido"]["cantidad"]) 
        cupon = datos_app.get("cupon", "") 
        
        # Conectado a la variable global PRECIO_UNITARIO
        total = Funciones.calcular_total_pagar(cantidad, PRECIO_UNITARIO, cupon)
        folio = random.randint(10000, 99999)
        
        # RESPALDO LOCAL EN CSV
        with open("nomina_despachos.csv", "a", encoding="utf-8") as bd:
            bd.write(f'{folio},{cliente},"{direccion}",{cantidad}\n')
            
        # --- NUEVO 2: ESCRITURA EN LA NUBE (GOOGLE SHEETS) ---
        if hoja_bd:
            try:
                # Calculamos la fecha en este instante
                fecha_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Escribimos los datos respetando el orden de tus columnas (A hasta G)
                hoja_bd.append_row([
                    folio, fecha_str, cliente, direccion, cantidad, cupon, total
                ])
            except Exception as e:
                print(f"Error interno al guardar en Google Sheets: {e}")
        # -----------------------------------------------------
            
        respuesta = {
            "exito": True,
            "folio": folio,
            "total_cobrado": total,
            "mensaje": f"¡Venta exitosa, {cliente}! Tu orden va en camino."
        }
        
        # Todo salió bien, devolvemos el recibo y un código 200 (OK en internet)
        return jsonify(respuesta), 200

    except (KeyError, ValueError, TypeError):
        # 2. Si falta un dato o la cantidad no es un número, el servidor atrapa el error
        respuesta_error = {
            "exito": False,
            "mensaje": "⚠️ Error en los datos recibidos. Por favor, revisa tu orden."
        }
        # Devolvemos el error a la app y un código 400 (Bad Request / Petición incorrecta)
        return jsonify(respuesta_error), 400
    
# Ruta 3: PANEL DE ADMINISTRACIÓN PROTEGIDO (GET)
@app.route('/admin/ventas', methods=['GET'])
def auditoria_remota():
    # 1. EL GUARDIA DE SEGURIDAD
    # Buscamos la palabra 'token' en la dirección web que ingresa el usuario
    llave_acceso = request.args.get("token")
    
    # Si la llave está vacía o no es exactamente nuestra contraseña secreta, bloqueamos el paso
    if llave_acceso != "superadmin2026":
        # Código 401 significa "No Autorizado" en el estándar de internet
        return jsonify({"error": "🔒 Acceso denegado. Credenciales inválidas."}), 401

    # 2. Si la llave es correcta, el código continúa normalmente hacia la bóveda
    total_unidades = 0
    
    try:
        with open("nomina_despachos.csv", "r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv, None) 
            
            for fila in lector_csv:
                if not fila:
                    continue
                cantidad_comprada = int(fila[-1])
                total_unidades += cantidad_comprada
                
        # Conectado a la variable global PRECIO_UNITARIO
        ingresos_totales = total_unidades * PRECIO_UNITARIO
        
        reporte = {
            "estado": "OK",
            "nivel_acceso": "Administrador",
            "metricas": {
                "unidades_despachadas": total_unidades,
                "ingresos_brutos": ingresos_totales
            }
        }
        
        return jsonify(reporte), 200

    except FileNotFoundError:
        return jsonify({"mensaje": "Aún no hay registros de ventas hoy."}), 404
    
if __name__ == '__main__':
    print("🌐 Iniciando servidor web blindado...")
    app.run(host='0.0.0.0', debug=True, port=5000)