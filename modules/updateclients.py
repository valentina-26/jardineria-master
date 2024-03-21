import json
import requests
import modules.getClients as gC
from tabulate import tabulate
import os



#NOMBRE
def NOMBREclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente=gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["nombre_cliente"] = input("ingrese el nuevo nombre del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")
        


#NOMBRE CONTACTO
def CONTACTOclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el cliente en el que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["nombre_contacto"] = input("Ingrese el nuevo nombre de contacto")
                    
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")
            
            
            

#APELLIDO CONTACTO
def CONAPclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["apellido_contacto"] = input("ingrese el nuevo apellido del contacto del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#TELEFONO
def TELEFONOclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar el telefono?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["telefono"] = input("ingrese el nuevo telefono del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#FAX
def FAXoficinaUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["fax"] = input("ingrese el nuevo fax del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#DIRECCION1
def DIRECCION1clieneUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["linea_direccion1"] = input("ingrese la nueva linea de direccion 1 del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#DIRECCION 2
def DIRECCION2clienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["linea_direccion2"] = input("ingrese la nueva linea de direccion 2 del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#CIUDAD
def CIUDADclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["ciudad"] = input("ingrese la nueva ciudad del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")




#REGION
def REGIONclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["region"] = input("ingrese la nueva region del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#PAIS
def PAISclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["pais"] = input("ingrese el nuevo pais del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")
            


#CODIGO POSTAL
def CODPOSclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["codigo_postal"] = input("ingrese el nuevo codigo postal del cliente: ")
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")


#CODIGO EMPLEADO VENTAS
def CODEMPVENclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["codigo_empleado_rep_ventas"] = int(input("ingrese el nuevo codigo del representante de ventas del cliente: "))
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")



#LIMITE CREDITO
def LIMITECREclienteUpdate(codigo):
    while True:
        if(codigo != None):
            cliente= gC.getClienteCodigoOTRO((codigo))
            if (cliente):
                print(tabulate(cliente, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el cliente que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    cliente[0]["limite_credito"] = int(input("ingrese el nuevo limite de credito del cliente: "))
                    peticion = requests.put(f'http://154.38.171.54:5001/cliente/{cliente[0].get("id")}', headers= headers, data= json.dumps(cliente[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el cliente {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del cliente")






def menu():
  while True:
    os.system("clear")
    print("""


                                             ACTUALIZAR
                                                         CLIENTES                     
                                                                                                 
                


                                 1. Nombre del cliente
                                 2. Nombre del contacto
                                 3. Apellido del contacto
                                 4. Telefono
                                 5. Fax
                                 6. Linea direccion 1
                                 7. Linea direccion 2
                                 8. Ciudad
                                 9. Region
                                 10. Pais
                                 11. Codigo Postal
                                 12. Codigo del empleado representante de ventas del cliente 
                                 13. Limite del credito
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigocliente = input(("Ingrese el codigo del cliente al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(NOMBREclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(CONTACTOclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(CONAPclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(TELEFONOclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(FAXoficinaUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(DIRECCION1clieneUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(DIRECCION2clienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(CIUDADclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==9):
            print(tabulate(REGIONclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==10):
            print(tabulate(PAISclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==11):
            print(tabulate(CODPOSclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==12):
            print(tabulate(CODEMPVENclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==13):
            print(tabulate(LIMITECREclienteUpdate(codigocliente), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break
        else:
                print("Elija algun número disponible del 0 al 13 ")
               
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 13")
        