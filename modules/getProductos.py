from tabulate import tabulate
import requests
import os


def getAllPRODUCTOS():
     peticion = requests.get(" http://154.38.171.54:5008/productos")
     data = peticion.json()
     return data
 
 
def getProductoCodigooo(codigo):
    peticion = requests.get("http://154.38.171.54:5008/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []
    
    
def getProductoCodigo(codigo):
    for val in  getAllPRODUCTOS():
        if(val.get("codigo") == codigo):
            return val
    
    
def getAllProveedor ():
    Nombre_proveedor =[ ] 
    for val in getAllPRODUCTOS():
       if(val.get("proveedor")=="Murcia Seasons"):
           Nombre_proveedor.append(val)
    return Nombre_proveedor

#(ejercicio  15 listado productos gama ornamentales
#con mas de 100 unidades en stock
#odenado de mayor a menor precio


def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in  getAllPRODUCTOS():
        if (val.get("gama") == gama and val.get("cantidad_en_stock")>= stock):
         condiciones.append(val)
    
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i,val in enumerate(condiciones):
        if(condiciones[i].get ("descripcion")):
            condiciones[i]["descripcion"]= f'{condiciones[i]["descripcion"][: 5]}...¡'

            condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta" : val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama" : val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "Proveedor" :val.get("proveedor"),
                "descripcion":f'{val.get("descripccion")[:5]}...' if condiciones[i].get ("descripcion") else None ,
                "stock": val.get("cantidad_en_stock"),
                "base":val.get("precio_proveedor"),
              
                }
    return condiciones







def menu():
    while True:
        os.system("clear")
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____ ____  __ ____  _  _  ___ ____ __  ____ 
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  _ (  _ \/  (    \/ )( \/ __|_  _)  \/ ___)
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) __/)   (  O ) D () \/ ( (__  )((  O )___ \
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (__) (__\_)\__(____/\____/\___)(__)\__/(____/
            
            0.Regresar
            1.obtener lista de todos los productos del proveedor "Murcia Seasons"
            2.obtener todos losproductos de una categoria ordenandosu preciode venta,tambien que su stock sea
            
    """)
        
        opcion = int(input("seleccione una de las opciones: "))
        
    
      
        if (opcion == 1):
                print(tabulate(getAllProveedor(), headers="keys", tablefmt="github"))
                    
        
        elif (opcion == 2):
                gama = (input("ingrese la gama que desea filtrar: "))
                stock =int(input("ingrese las unidades de stock.  "))
                print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))

        elif (opcion == 0 ):
            break