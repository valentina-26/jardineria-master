import os
import json
from tabulate import tabulate 
import modules.getGama as gG
import requests
import re
import modules.getProductos as gP


def GuardarProducto():
        

    producto = dict()

    while True:
        try:
            
            #CODIGO
            if not producto.get("codigo_producto"):
             codigo = input("Ingrese el codigo del producto: ")
            if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                if gP.getProductoCodigo(codigo):
                    raise Exception("El codigo ingresado ya existe.")
                else:
                    producto["codigo_producto"] = codigo
            else:
                raise Exception(f"El codigo no cumple con el estandar establecido ( ejm: XX-111 ).")      
                


            #NOMBRE
            # validacion de cadena solo  letras primera Mayus
            if(not producto.get("nombre")):
                nombre = input("ingrese el nombre del producto")
                if(re.match(r'^[A-Z][a-z]*\s*)+$',nombre)is not None):
                    producto["nombre"] = nombre
                    break
                else:
                    raise Exception("el nombre del producto no cumple con el estandar establecido")
                

            #DIMENSIONES
            # VALIDAR NUMEROS
            if not producto.get("dimensiones"):
                dimensiones = input("ingrese las dimensiones del producto: ")
                if(re.match) (r'^\d+-\d+$', dimensiones) is not None:
                    producto[dimensiones] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                    
            # PROVEEDOR
            #VALIDAR LETRAS,SOLO  PRIMERA EN MAYUSCULA
            if not producto.get("proveedor"):
                proveedor = input("ingrese el proveedor del producto: ")
                if(re.match) (r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto[proveedor] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                    
            #DESCRIPCION
            if not producto.get("descripcion"):
                descripcion= input("ingrese la descripcion del producto del producto: ")
                producto[descripcion] = descripcion
                    
            #CANTIDAD EN STOCK

            if not producto.get("cantidad_en_stock"):
                cantidad_en_stock= input("ingrese la cantidad en stock  del producto: ")
                if(re.match) (r'^[0-9]+$', cantidad_en_stock) is not None:
                    cantidad_en_stock = int (cantidad_en_stock)
                    producto[cantidad_en_stock] = cantidad_en_stock
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO VENTA

            if not producto.get("precio_venta"):
                precio_venta= input("ingrese el precio de venta del producto: ")
                if(re.match) (r'^[0-9]+$', precio_venta) is not None:
                    precio_venta = int (precio_venta)
                    producto[precio_venta] = precio_venta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO PROVEEDOR

            if not producto.get("precio_proveedor"):
                precio_proveedor= input("ingrese el precio proveedor del producto: ")
                if(re.match) (r'^[0-9]+$', precio_proveedor) is not None:
                    precio_proveedor = int (precio_proveedor)
                    producto[precio_proveedor] = precio_proveedor
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
            
        except Exception as error:
            print(error)                        
                


    peticion = requests.post(" http://172.16.100.130:5500",data=json.dumps(producto, indent=4).encode("UTF-8"))
    res =peticion.json()
    res["Mensaje"] = "producto guardado exitosamente"
    return [res]

# def deleteProducto(id):
#     if = (len(gP.getproductCodigo(id)))
#     peticion =  requests.delete(" http://172.16.100.130:5500/producto/{id}")
#     print(peticion)
#     return[res]

def menu():
    while True:
        print("""
  __   ___  __  __  __  _  _  __  ___  ____  ___    __   ___     ___   __  ____  __   ___    ___  ___    ___  ___   __  ___  _  _  __  ____  __   ___ 
 (  ) (   \(  \/  )(  )( \( )(  )/ __)(_  _)(  ,)  (  ) (  ,)   (   \ (  )(_  _)/  \ / __)  (   \(  _)  (  ,\(  ,) /  \(   \( )( )/ _)(_  _)/  \ / __)
 /__\  ) ) ))    (  )(  )  (  )( \__ \  )(   )  \  /__\  )  \    ) ) )/__\  )( ( () )\__ \   ) ) )) _)   ) _/ )  \( () )) ) ))()(( (_   )( ( () )\__ \
(_)(_)(___/(_/\/\_)(__)(_)\_)(__)(___/ (__) (_)\_)(_)(_)(_)\_)  (___/(_)(_)(__) \__/ (___/  (___/(___)  (_)  (_)\_)\__/(___/ \__/ \__) (__) \__/ (___/
                    
                
                    1.Guardar un producto nuevo
                    2. eliminar un producto
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(GuardarProducto(),headers="keys",tablefmt="github"))
                    input("precione una tecla para continuar ......")
        # if (opcion == 2): 
        #     idproducto = input("ingrese elid del producti que desea eliminar. ")
        #     print(tabulate(deleteProducto(idproducto)["body"],headers = "keys",tablefmt="github"))
            
            
        elif (opcion == 0):
            break
            
            