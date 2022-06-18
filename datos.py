#ACA SE GUARDAN DATOS IMPORTANTES QUE DESPUES VOY A IMPORTAR!
import requests

#Api de terceros NASA
url = 'https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY'
http_rsp = requests.get(url)
cuadros_rsp = http_rsp.json() #Este es el diccionario de la nasa ya en formato json


#Datos que vamos a usar: ID y imagen
cuadros = []

for cuadro in cuadros_rsp:
    cuadros.append(cuadro['identifier'])
    cuadros.append(cuadro['image'])
    imagen = cuadro['image']



#Lista de medidas
medidas = [
    {"medida": "18x24","precio": "$800"},
    {"medida": "20x30","precio": "$1000"},
    {"medida": "30x40","precio": "$1500"},
    {"medida": "40x40","precio": "$2000"},
    {"medida": "40x50","precio": "$2300"},
    {"medida": "50x70","precio": "$3000"},
    {"medida": "70x80","precio": "$3500"},
    {"medida": "80x100","precio": "$4000"}
]

class CuadroNuevo:
    def __init__(self, medidas, precio):
        self.medidas = medidas
        self.precio = precio

    def __str__(self):
        return f'\t ======= Tu cuadro personalizado es: ======= \n' \
               f'\t Medidas:{self.medidas} \n' \
               f'\t Precio: {self.precio} \n' \
               f' Para terminar tu compra e ir al carrito ingrese la opcion 3), si quiere seguir comprando seleccione la opcion 1)'