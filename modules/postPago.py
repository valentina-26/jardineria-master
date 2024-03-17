import json
import requests
from tabulate import tabulate
import os


def GuardarPago():

    guardar = { 
        "codigo_cliente": int(input("ingrese el codigo del cliente: ")),
        "forma_pago": int(input("ingrese el metodo de pago: ")),
        "Id_transaccion":int(input("ingrese el ID de la transaccion: ")),
        "fecha_pago":int(input("ingrese la fecha del pago(año/mes/dia): ")),
        "extension":int(input("ingrese la extension del empleado: ")),
        "total":int(input("ingrese el total del pago: ")),
        "codigo_oficina":int(input("ingrese el codigo d la oficina")),

    }


    peticion = requests.get("http://172.16.103.34:5505",data=json.dumps(guardar, indent=4).encode("UTF-8"))
    res = peticion.json.json()
    res["mensaje"] = "Pago guardado exitosamnete"
    return[res]




def menu():
    while True:
        print("""
   __  ___ __  __ __ _  _ __ ___ ____ ___   __  ___     ___  __ ____ __  ___ 
 (  )(   (  \/  |  | \( |  ) __|_  _|  ,) (  )(  ,)   (   \(  |_  _)  \/ __)
 /__\ ) ) )    ( )( )  ( )(\__ \ )(  )  \ /__\ )  \    ) ) )__\ )(( () )__ \
(_)(_|___(_/\/\_|__|_)\_|__|___/(__)(_)\_|_)(_|_)\_)  (___(_)(_|__)\__/(___/
(   (  _)  (  ,(  )/ _)/  \                                                 
 ) ) ) _)   ) _/__( (/( () )                                                
(___(___)  (_)(_)(_)__/\__/                                                                   
                
                    1.Guardar un producto nuevo
                    0.regresar al menu principal  
                
                    
                
            """)