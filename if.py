#ACA RESOLVIMOS USANDO IF

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
            print(f'Ingrese la opcion 2) para personalizar su cuadro! \n')



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
            precio = 0

            if medidas == '1':
                    medidas1 = '18x24'
                    precio1 = 800
                    medidas = medidas1
                    precio = precio1
                    print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '2':
                medidas2 = '20x30'
                precio2 = 1000
                medidas = medidas2
                precio = precio2
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '3':
                medidas3 = '30x40'
                precio3 = 1500
                medidas = medidas3
                precio = precio3
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '4':
                medidas4 = '40x40'
                precio4 = 2000
                medidas = medidas4
                precio = precio4
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '5':
                medidas5 = '40x50'
                precio5 = 2300
                medidas = medidas5
                precio = precio5
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '6':
                medidas6 = '50x70'
                precio6 = 3000
                medidas = medidas6
                precio = precio6
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '7':
                medidas7 = '70x80'
                precio7 = 3500
                medidas = medidas7
                precio = precio7
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            elif medidas == '8':
                medidas8 = '70x100'
                precio8 = 4000
                medidas = medidas8
                precio = precio8
                print(f'Se agrego al carrito tu cuadro de: {medidas}, con un monto de: {precio}')
            else:
                print('Opcion invalida, ingrese otra opcion')

            mi_cuadro = CuadroNuevo(medidas, precio)
            print(mi_cuadro)

            dict = {}
            dict["ID cuadro"] = id_cuadro
            dict["Medidas del cuadro"] = medidas
            dict["Precio del cuadro"] = precio
            compras.append(dict)

        elif option == '3':
            print(f"Listado de compras: {compras}")


        elif option == '4':
            print('El programa finalizo, gracias por comprar en Cuadros Espaciales')
            print('Que tenga un hermoso dia! :)')
            break

        else:
            print('Opcion invalida. Ingrese una opcion valida')

# CODIGO:

menu()
