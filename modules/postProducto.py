import os
import json
from tabulate import tabulate 
import modules.getGama as gG
import requests

def postProducto():
    #json-server storage/producto.json -b 5003
    producto= {
        "codigo_producto":input("ingrese elcodigo delproducto"),
        "nombre": input("ingrese el nombre delproducto"),
        "gama": gG.getAllNombre()[int(input("Seleccione la gama\n: "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones":input("ingrese la dimension delproducto"),
        "proveedor": input("ingrese elproveedor delproducto"),
        "descripcion": input("ingrese la descripcion delproducto"),
        "cantidad_en_stock": input("ingrese  la cantidad destock"),
        "precio_venta": input("ingrese elprecio de ventas"),
        "precio_proveedor": input("ingrese elprecio delproveedor")
              }


    peticion = requests.post("http://172.16.100.130:5002",data=json.dumps(producto, indent=4).encode("UTF-8"))
    res =peticion.json()
    res["Mensaje"] = "producto guardado"
    return res

def menu():
    while True:
        print("""
  __   ___  __  __  __  _  _  __  ___  ____  ___    __   ___     ___   __  ____  __   ___    ___  ___    ___  ___   __  ___  _  _  __  ____  __   ___ 
 (  ) (   \(  \/  )(  )( \( )(  )/ __)(_  _)(  ,)  (  ) (  ,)   (   \ (  )(_  _)/  \ / __)  (   \(  _)  (  ,\(  ,) /  \(   \( )( )/ _)(_  _)/  \ / __)
 /__\  ) ) ))    (  )(  )  (  )( \__ \  )(   )  \  /__\  )  \    ) ) )/__\  )( ( () )\__ \   ) ) )) _)   ) _/ )  \( () )) ) ))()(( (_   )( ( () )\__ \
(_)(_)(___/(_/\/\_)(__)(_)\_)(__)(___/ (__) (_)\_)(_)(_)(_)\_)  (___/(_)(_)(__) \__/ (___/  (___/(___)  (_)  (_)\_)\__/(___/ \__/ \__) (__) \__/ (___/
            
           
            1.Guardar un producto nuevo
            0.regresar al menu principal  
          
              
           
    """)
        
        opcion = int(input("seleccione una de las opciones: "))
        
        if (opcion == 1):
            print(tabulate(postProducto(),headers="keys",tablefmt="github"))
            input("precione una tecla para continuar ......")

        elif (opcion == 0):
            break    
       