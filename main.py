from flask import Flask, jsonify, request
from datos import medidas
from datos import cuadros_rsp
from datos import cuadros
from datos import imagen
from datos import CuadroNuevo
app = Flask(__name__)

#ACA GENERAMOS LA API DE TERCEROS DE LA NASA
@app.route('/nasa', methods=['GET'])
def nasaGet():
    return jsonify({'cuadros:': cuadros_rsp, 'status': 'ok'})


#ACA HACEMOS QUE DE LA API DE LA NASA NOS TRAIGA ID Y IMAGEN
@app.route('/cuadros', methods=['GET'])
def imagenesGet():
    return jsonify({'imagenes disponibles:': cuadros, 'status': 'ok'})


#ACA EL CLIENTE ELIGE LA IMAGEN
@app.route('/imagen/<id>', methods=['GET'])
def imagenGet(id):
    return f'ID imagen:{id} \n '\
           f'Imagen: {imagen}' \



#ACA GENERAMOS LA TABLA DE MEDIDAS
@app.route('/medidas', methods=['GET'])
def medidasGet():
    return jsonify({'medidas:': medidas, 'status': 'ok'})




#ACA GENERAMOS EL CUADRO PERSONALIZADO
cuadros_nuevos : list = []
@app.route('/micuadro', methods=['POST'])
def micuadroPost():
    cuadro = request.json
    try:
        cuadro_nuevo = CuadroNuevo(
        cuadro['medidas'],
        cuadro['precio'])
        cuadros_nuevos.append(cuadro_nuevo)
    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400








'''#ACA GENERAMOS EL CARRITO
@app.route('/carrito', methods=['POST'])
def carritoPost():
    body = request.json
    id = body['ID']
    medidas= body['medidas']
    precio = body['precio']'''







#ESTO SIMEPRE VA AL FINAL!!
if __name__ == '__main__':
    app.run(debug=True, port=4000)
