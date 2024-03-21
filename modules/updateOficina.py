import json
import requests
import modules.getOficina as getOfi
from tabulate import tabulate
import os




#CIUDAD
def CIUDADoficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["ciudad"] = input("ingrese la nueva ciudad de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
#PAIS
def PAISoficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina en el que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["pais"] = input("Ingrese el nuevo pais de la oficina")
                    
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
            
#REGION
def REGIONoficnaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["region"] = input("ingrese la nueva region de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
            
#CODIGO POSTAL
def CODPOSoficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["codigo_postal"] = input("ingrese el nuevo codigo postal de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
            
#TELEFONO 
def TELEFONOoficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["telefono"] = input("ingrese el nuevo telefono de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")  
            
            
#LINEA DIRECCION  1
def LINDI1oficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar  1?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["linea_direccion1"] = input("ingrese la nueva linea de direccion 1 de la oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
            
#LINEA DIRECCION 2  
def LINDI2oficinaUpdate(codigo):
    while True:
        if(codigo != None):
            oficina= getOfi.getOficinaCodigosOTRO((codigo))
            if (oficina):
                print(tabulate(oficina, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Esta es la oficina que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    oficina[0]["linea_direccion2"] = input("ingrese la nueva linea de direccion 2: ")
                    peticion = requests.put(f'http://154.38.171.54:5005/oficinas/{oficina[0].get("id")}', headers= headers, data= json.dumps(oficina[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"la oficina {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo de la oficina")
            
            
            
            
            
            
def menu():
  while True:
    os.system("clear")
    print("""

                  
                            ACTUALIZAR 
                                       PRODUCTOS                                                                 


                                 1. Ciudad de la Oficina
                                 2. Pais de la oficina
                                 3. Region de la oficina
                                 4. Codigo postal de la oficina
                                 5. Telefono de la oficina
                                 6. Linea de direccion 1 de la oficina
                                 7. Linea de direccion 2 de la oficina
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigooficina = input(("Ingrese el codigo de la oficina al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(CIUDADoficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(PAISoficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(REGIONoficnaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(CODPOSoficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(TELEFONOoficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(LINDI1oficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(LINDI2oficinaUpdate(codigooficina), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 7 ")
               
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 7")
                  
            
            
 
        