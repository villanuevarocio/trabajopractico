#LISTAS.
#ACA ACTUALIZARIAMOS LOS PRECIOS MAS FACIL

import requests
from cuadros import Cuadro
from cuadros import CuadroNuevo
from colorama import Fore, init
init()

#esto se puede borrar
medida1 = {"medida": "18x24","precio": "$800"}
medida2 = {"medida": "20x30","precio": "$1000"}
medida3 = {"medida": "30x40","precio": "$1500"}
medida4 = {"medida": "40x40","precio": "$2000"}
medida5 = {"medida": "40x50","precio": "$2300"}
medida6 = {"medida": "50x70","precio": "$3000"}
medida7 = {"medida": "70x80","precio": "$3500"}
medida8 = {"medida": "80x100","precio": "$4000"}

lista_medidas = [medida1, medida2, medida3, medida4, medida5, medida6, medida7, medida8]

#hasta aca se puede borrar

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
                for medidas_dict in lista_medidas:
                    for medida in medidas_dict:
                        {print(f' Medida: {medidas_dict["medida"]}')}
                        {print(f' Precio: {medidas_dict["precio"]}')}
            else:
                pass


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


#CODIGO:

menu()




'''lista_medidas = [{"medida": "18x24","precio": "$800"},
                 {"medida": "20x30","precio": "$1000"},
                 {"medida": "30x40","precio": "$1500"},
                 {"medida": "40x40","precio": "$2000"},
                 {"medida": "40x50","precio": "$2300"},
                 {"medida": "50x70","precio": "$3000"},
                 {"medida": "70x80","precio": "$3500"},
                 {"medida": "80x100","precio": "$4000"}]'''


