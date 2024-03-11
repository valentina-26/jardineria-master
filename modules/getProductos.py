from tabulate import tabulate

import storage.producto as pro

def getAllProveedor():
    Nombre_proveedor =[ ] 
    for val in pro.produto:
       if(val.get("proveedor")=="Murcia Seasons"):
           Nombre_proveedor.append(val)
    return Nombre_proveedor

#(ejercicio  15 listado productos gama ornamentales
#con mas de 100 unidades en stock
#odenado de mayor a menor precio


def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in  pro.producto:
        if (val.get("gama") == gama and val.get("precio_venta")>= stock):
         condiciones.append(val)
    
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(keys=price)


def menu():
    while True:
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____ ____  __ ____  _  _  ___ ____ __  ____ 
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  _ (  _ \/  (    \/ )( \/ __|_  _)  \/ ___)
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) __/)   (  O ) D () \/ ( (__  )((  O )___ \
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (__) (__\_)\__(____/\____/\___)(__)\__/(____/
            
            0.Regresar
            1.obtener lista de todos los productos del proveedor "Murcia Seasons"
        
            
           
    """)
    
    
        opcion = int(input("seleccione una de las opciones: "))


            
        if (opcion == 1):
                print(tabulate(getAllProveedor(), headers="keys", tablefmt="github"))
                
        elif(opcion == 0):
            break