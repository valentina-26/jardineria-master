import json
import requests
import modules.getPedido as gped
from tabulate import tabulate
import os




#FECHA
def FECHApedioUpdate(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_pedido"] = input("ingrese la nueva fecha del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
            
            
#FECHA ESPERADA
def FESPERADApedidoUPDATE(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido en el que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_esperada"] = input("Ingrese la nueva fecha esperada del pedido")
                    
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
            
            
            
#FECHA DE DENTREGA
def FENTREGApedidoUpdate(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido que desea actualizar?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_entrega"] = input("ingrese la nueva fecha de entrega del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")   
            
            
            
#ESTADO
def EStADOpedidoUpdate(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["estado"] = input("ingrese el nuevo estado del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")     
            
            
            
#COMENTARIO
def COMENTARIOpedidoUpdate(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["comentario"] = input("ingrese el nuevo comentario del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")     
            
            
#CLIENTE
def CLIENTEpedidoUpdate(codigo):
    while True:
        if(codigo != None):
            pedido= gped.getPedidoCodigoOTRO((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el pedido que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["codigo_cliente"] = int(input("ingrese el nuevo codigo del cliente del pedido: "))
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
            
            
            
            
            
def menu():
  while True:
    os.system("clear")
    print("""


                                 
                            UPDATE
                                   DE 
                                      PEDIDO                                                                 
                        


                                 1. Fecha del pedido
                                 2. Fecha esperada
                                 3. Fecha de entrega
                                 4. Estado del pedido
                                 5. Comentario del pedido
                                 6. Codigo del cliente

                                 0. Salir
""")


    opcion= int(input("\nSeleccione el dato que quiera editar: "))
    codigopedido = input(("Ingrese el codigo del pedido al que deseas actualizar los datos: "))
    if (opcion == 1):
        print(tabulate(FECHApedioUpdate(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==2):
        print(tabulate(FESPERADApedidoUPDATE(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==3):
        print(tabulate(FENTREGApedidoUpdate(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==4):
        print(tabulate(EStADOpedidoUpdate(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==5):
        print(tabulate(COMENTARIOpedidoUpdate(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==6):
        print(tabulate(CLIENTEpedidoUpdate(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==0):
        break                
                       