from tabulate import tabulate

import storage.producto as pro

def getAllProveedor():
    Nombre_proveedor =[ ] 
    for val in pro.produto:
       if(val.get("proveedor")=="Murcia Seasons"):
           Nombre_proveedor.append(val)
    return Nombre_proveedor

def menu():

 print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____ ____  __ ____  _  _  ___ ____ __  ____ 
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  _ (  _ \/  (    \/ )( \/ __|_  _)  \/ ___)
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) __/)   (  O ) D () \/ ( (__  )((  O )___ \
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (__) (__\_)\__(____/\____/\___)(__)\__/(____/
            
            
            
            
            
            
            
            
            

            
            
            1.obtener lista de todos los productos del proveedor "Murcia Seasons"
        
            
           
    """)
    
    
opcion = int(input("seleccione una de las opciones: "))


    
if (opcion == 1):
        print(tabulate(getAllProveedor(), headers="keys", tablefmt="github"))



