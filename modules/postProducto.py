import os
import json
from tabulate import tabulate 
import modules.getGama as gG
import requests
import re
import modules.getProductos as gP

def postProducto():
    #json-server storage/producto.json -b 5003
        producto = dict()

        while True:
            try:
        #CODIGO
        #validacion codigo(mayusculas,numeros y signos)
                if(not producto.get("codigo_producto")):
                    codigo=input("ingrese elcodigo del producto: ")
                    if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                        data = gP.getproductCodigo(codigo)
                        if (data):
                            print(tabulate(data, headers="keys",tablefmt="github"))
                            raise Exception("el codigo producto ya existe")
                        else:
                            producto["codigo_producto"] = codigo

                    else:
                        raise Exception("el codigo producto no cumple con el estantar")
                

        #NOMBRE
        # validacion de cadena solo  letras primera Mayus
                if(not producto.get("nombre")):
                    nombre = input("ingrese el nombre del producto")
                    if(re.match(r'^[A-Z][a-z]*\s*)+$',nombre)is not None):
                        producto["nombre"] = nombre
                        break
                    else:
                        raise Exception("el nombre del productono cumple con el estandar establecido")
                    
            except Exception as error:
                print(error)

        #DIMENSIONES
        # VALIDAR NUMEROS
        codigo=input("ingrese elcodigo del producto: ")
        if(re.match(r'^[0-9]$', codigo)is not None):
    



            
    # producto= {
    #     "codigo_producto":input("ingrese elcodigo delproducto"),
    #     "nombre": input("ingrese el nombre delproducto"),
    #     "gama": gG.getAllNombre()[int(input("Seleccione la gama\n: "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
    #     "dimensiones":input("ingrese la dimension delproducto"),
    #     "proveedor": input("ingrese elproveedor delproducto"),
    #     "descripcion": input("ingrese la descripcion delproducto"),
    #     "cantidad_en_stock": input("ingrese  la cantidad destock"),
    #     "precio_venta": input("ingrese elprecio de ventas"),
    #     "precio_proveedor": input("ingrese elprecio delproveedor")
    #           }


    # peticion = requests.post("http://172.16.100.130:5002",data=json.dumps(producto, indent=4).encode("UTF-8"))
    # res =peticion.json()
    # res["Mensaje"] = "producto guardado"
    # return res

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
       