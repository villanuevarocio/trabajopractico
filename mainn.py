import requests
from cuadros import Cuadro
from cuadros import CuadroNuevo
from colorama import Fore, init
init()

url = 'https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY'

http_rsp = requests.get(url)
cuadros_rsp = http_rsp.json()

#print(cuadros_rsp)   ESTE ES EL DICCIONARIOOO

cuadros = []
compras = []

for cuadro in cuadros_rsp:
    cuadros.append(Cuadro(cuadro['identifier'], cuadro['image']))


def menu():
    print(Fore.MAGENTA + '### IMAGENES ESPACIALES ###')
    print(Fore.RESET)

    while True:
        print('1) Seleccionar imagen del cuadro')
        print('2) Personaliza tu cuadro')
        print("3) Carrito")
        print('4) Salir del programa')

        option = input('<<')

        if option == '1':
            for cuadro in cuadros:
                print(cuadro)
            print('Coloca el ID de la imagen que desee')
            id_cuadro = input('<<')



        elif option == '2':
            print('Selecciona la medida que desees')
            print("Medidas posibles:")
            print("1) 18x24 --> PRECIO: $800")
            print("2) 20x30 --> PRECIO $1000")
            print("3) 30x40 --> PRECIO: $1500")
            print("4) 40x40 --> PRECIO: $2000")
            print("5) 40x50 --> PRECIO: $2300")
            print("6) 50x70 --> PRECIO: $3000")
            print("7) 70x80 --> PRECIO: $3500")
            print("8) 70x100 --> PRECIO: $4000")

            medidas = input('Coloca la opcion que desees: >>')

            print('Elije la opcion que desee: Galaxia, Estrellas o Agujero negro')
            imagen = input('<<')

            mi_cuadro = CuadroNuevo(medidas, imagen)
            print(mi_cuadro)

            dict = {}
            dict["ID cuadro"] = id_cuadro
            dict["Medidas del cuadro"] = medidas
            dict["Diseño del cuadro"] = imagen
            compras.append(dict)

        elif option == '3':
            print(f"Listado de compras {compras}")


        elif option == '4':
            break

        else:
            print('Opcion invalida. Ingrese una opcion valida')


#CODIGO:

menu()
print('Hola)
