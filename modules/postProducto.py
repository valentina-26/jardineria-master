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
                raise Exception("El codigo no cumple con el estandar establecido ejm: XX-444 ")      
                


            #NOMBRE
            # validacion de cadena solo  letras primera Mayus
            if not producto.get("nombre"):
                nombre = input(f"Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, por favor  todas las palabras deben iniciar con mayúsculas.")
                

            #DIMENSIONES
            # VALIDAR NUMEROS
            if not producto.get("dimensiones"):
                dimensiones = input("ingrese las dimensiones del producto: ")
                if(re.match) (r'^\d+-\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                    
            # PROVEEDOR
            #VALIDAR LETRAS,SOLO  PRIMERA EN MAYUSCULA
            if not producto.get("proveedor"):
                proveedor = input("ingrese el proveedor del producto: ")
                if(re.match) (r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                    
            #DESCRIPCION
            if not producto.get("descripcion"):
                descripcion= input("ingrese la descripcion del producto del producto: ")
                producto["descripcion"] = descripcion
                    
            #CANTIDAD EN STOCK

            if not producto.get("CantidadEnStock"):
                CantidadEnStock= input("ingrese la cantidad en stock  del producto: ")
                if(re.match) (r'^[0-9]+$', CantidadEnStock) is not None:
                    CantidadEnStock = int (CantidadEnStock)
                    producto["CantidadEnStock"] = CantidadEnStock
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO VENTA

            if not producto.get("precio_venta"):
                precio_venta= input("ingrese el precio de venta del producto: ")
                if(re.match) (r'^[0-9]+$', precio_venta) is not None:
                    precio_venta = int (precio_venta)
                    producto["precio_venta"] = precio_venta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO PROVEEDOR

            if not producto.get("precio_proveedor"):
                precio_proveedor= input("ingrese el precio proveedor del producto: ")
                if(re.match) (r'^[0-9]+$', precio_proveedor) is not None:
                    precio_proveedor = int (precio_proveedor)
                    producto["precio_proveedor"] = precio_proveedor
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
            
        except Exception as error:
            print(error)                        
                


        peticion = requests.post("http://154.38.171.54:5008/productos",data=json.dumps(producto, indent=4).encode("UTF-8"))
        res =peticion.json()
        res["Mensaje"] = "producto guardado exitosamente"
        return [res]





def DeleteProducto(id):
    data = gP.DeleteProducto(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Producto no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
        
        return [res]
        
        
        
        
        
        
        
    

def menu():
    while True:
        print("""
                                        ADMINISTRAR
                                                   DATOS
                                                        DE
                                                          PRODUCTOS
                                                          
                                                          
                                                          
                    1.Guardar un producto nuevo
                    2. eliminar un producto
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(GuardarProducto(),headers="keys",tablefmt="github"))
                    input("precione una tecla para continuar ......")
                    
        elif opcion == 2:
            idProducto = input("Ingrese el id del producto: ")
            print(tabulate(DeleteProducto(idProducto), headers="keys", tablefmt="github"))
            input("precione una tecla para continuar:......")
            
            
        elif (opcion == 0):
            break
            
            