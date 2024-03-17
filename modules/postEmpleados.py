import json
import requests
from tabulate import tabulate
import os

def GuardarEmpleado():

    guardar = { 
        "codigo_empleado": int(input("ingrese el codigo empleado: ")),
        "nombre": int(input("ingrese el nombre del empleado: ")),
        "apellido1":int(input("ingrese el primer apellido: ")),
        "apellido2":int(input("ingrese el segundo apellido: ")),
        "extension":int(input("ingrese la extension del empleado: ")),
        "email":int(input("ingrese el email del empleado: ")),
        "codigo_oficina":int(input("ingrese el codigo d la oficina")),
        "codigo_jefe":int(input("ingrese el codigo del jefe")),
        "puesto":int(input("ingrese el puesto dl empleado"))

    }


    peticion = requests.get("http://172.16.103.34:5502",data=json.dumps(guardar, indent=4).encode("UTF-8"))
    res = peticion.json.json()
    res["mensaje"] = "Empleado guardado exitosamnete"
    return[res]




def menu():
    while True:
        print("""
  __  ___ __  __ __ _  _ __ ___ ____ ___   __  ___     ___  __ ____ __  ___ 
 (  )(   (  \/  |  | \( |  ) __|_  _|  ,) (  )(  ,)   (   \(  |_  _)  \/ __)
 /__\ ) ) )    ( )( )  ( )(\__ \ )(  )  \ /__\ )  \    ) ) )__\ )(( () )__ \
(_)(_|___(_/\/\_|__|_)\_|__|___/(__)(_)\_|_)(_|_)\_)__(___(_)(_|__)\__/(___/
(   (  _)  (  _|  \/  |  ,(  ) (  _)(  )(   \ /  \/ __)                     
 ) ) ) _)   ) _))    ( ) _/)(__ ) _)/__\ ) ) | () )__ \                     
(___(___)  (___|_/\/\_|_) (____|___|_)(_|___/ \__/(___/                     
                
                    1.Guardar un producto nuevo
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(GuardarEmpleado(),headers="keys",tablefmt="github"))
                    input("Precione una tecla para continuar ......")

        elif (opcion == 0):
            break
            