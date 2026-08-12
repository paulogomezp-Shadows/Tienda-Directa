from flask import Flask, jsonify, request
import random
import Funciones
import csv

app = Flask(__name__)

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
        
        total = Funciones.calcular_total_pagar(cantidad, 25000, cupon)
        folio = random.randint(10000, 99999)
        
        with open("nomina_despachos.csv", "a", encoding="utf-8") as bd:
            bd.write(f'{folio},{cliente},"{direccion}",{cantidad}\n')
            
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
    precio_producto = 25000
    
    try:
        with open("nomina_despachos.csv", "r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv, None) 
            
            for fila in lector_csv:
                if not fila:
                    continue
                cantidad_comprada = int(fila[-1])
                total_unidades += cantidad_comprada
                
        ingresos_totales = total_unidades * precio_producto
        
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