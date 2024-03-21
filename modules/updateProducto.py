import json
import requests
import modules.getProductos as gP
from tabulate import tabulate
import os



#NOMBRE
def NOMBREproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar el nombre?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["nombre"] = input("ingrese el nuevo nombre del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")
            
            
            
            
#GAMA
 
def GAMAproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto en el que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["gama"] = input(f"""
                    
                Gamas establecidas:
                                                  
                -Herbaceas
                -Herramientas
                -Aromáticas
                -Frutales
                -Ornamentales
                -Herramientas
                
                por favor ingrese la gama que desee: """)
                    
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")  
            
            
            
#DIMENSIONES
def DIMENSIONESproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["dimensiones"] = input("ingrese las nuevas dimensiones del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")                     
            
            
            
#PROVEEDOR
def PROVEEDORproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["proveedor"] = input("ingrese el nuevo nombre del proveedor: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")    
            
            
            
#DESCRIPCION
def DESCRIPCCIONproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["descripcion"] = input("ingrese la nueva descripcion del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")                   
            
            
            
#CANTIDAD EN STOCK
def STOCKproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["cantidad_en_stock"] = int(input("ingrese la nueva cantidad en stock del producto: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")            
            
            
            
#PRECIO VENTA
def PVENTAproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["precio_venta"] = int(input("ingrese la nueva cantidad del precio de venta: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")  
            
            
#PRECIO PROVEEDOR
def PPROVEEDORproductoUpdate(codigo):
    while True:
        if(codigo != None):
            producto= gP.getProductoCodigoOTRO((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el producto que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["precio_proveedor"] = int(input("ingrese la nueva cantidad del precio de proveedor: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")   
            
            
            
                              
            
            
            
            
            
def menu():
  while True:
    os.system("clear")
    print("""

                                        UPDATE 
                                                DE
                                                    PRODUCTOS             


                                 1. Nombre
                                 2. Gama
                                 3. Dimensiones
                                 4. Proveedor
                                 5. Descripcion
                                 6. Cantidad en Stock
                                 7. Precio de venta
                                 8. Precio de proveedor
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigoProducto = input(("Ingrese el codigo del producto al que deseas actualizar: "))
        
        
        if (opcion == 1):
            print(tabulate(NOMBREproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(GAMAproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(DIMENSIONESproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(PROVEEDORproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(DESCRIPCCIONproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(STOCKproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(PVENTAproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(PPROVEEDORproductoUpdate(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break   
        
        
         
        else:
            print("Elija algun número disponible del 0 al 8 ")
            
            
    except ValueError: 
         print("Por favor solo elija un numero del 0 al 8")
       