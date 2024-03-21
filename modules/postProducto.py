import os
import json
from tabulate import tabulate 
import modules.getGama as gG
import requests
import re
import modules.getProductos as gP
import modules.updateProducto as UP


def GuardarProducto():
    producto = dict()
    while True:
        try:
            
            
            #CODIGO
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del prodcuto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                    if gP.getProductoCodigo(codigo):
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo no cumple con el estandar por favor:ejm XX-111")
                
                
             #NOMBRE   
                
            if not producto.get("nombre"):
                nombre = input("Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, por favor todas las palabras iniciar con mayúsculas.")
                
                
                
            #GAMA    
            if not producto.get("gama"):
                gama = input("Ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', nombre) is not None:
                        producto["gama"] = gama
                else:
                    raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                
                
            #DIMENSIONES
            if not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if re.match(r'^\d+-\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas intente asi: numero-numero ")
                
                
            #PROVEEDOR    
            if not producto.get("proveedor"): 
                proveedor = input("Ingrese el proveedor: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("Proveedor no valido, por favor ingrese la primera letra en MAYUSCULA")
            
            
            #DESCRIPCION   
            if not producto.get("descripcion"):
                descripcion = input("Ingrese una descripción: ")
                producto["descripcion"] = descripcion
            
            
            #CANTIDAD STOCK
            if not producto.get("cantidadEnStock"):
                cantidad = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', cantidad) is not None:
                    cantidad = int(cantidad)
                    producto["cantidadEnStock"] = cantidad
                else:
                    raise Exception("Cantidad no valida, por favor ingrese solo digitos numericos.")
                
                
            #PRECIO VENTA   
            if not producto.get("precio_venta"):
                PrecioVenta = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', PrecioVenta) is not None:
                    PrecioVenta = int(PrecioVenta)
                    producto["precio_venta"] = PrecioVenta
                else:
                    raise Exception("Precio de venta no valido, por favor ingrese solo dígitos numéricos.")
                
                
            #PROVEEDOR    
            if not producto.get("precio_proveedor"):
                PrecioProveedor = input("Ingrese el precio del proveedor: ")
                if re.match(r'^[0-9]+$', PrecioProveedor) is not None:
                    PrecioProveedor = int(PrecioProveedor)
                    producto["precio_proveedor"] = PrecioProveedor
                    break
                else:
                    raise Exception("Precio de proveedor no valido, porfavor solo dígitos numéricos.")
        
        except Exception as error:
            print(error)                     
    
    peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
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

    asdasdasdasd =dict()
    return asdasdasdasd
        
        

        
        
        
        
        
        
        
    

def menu():
    while True:
        print("""
                                        ADMINISTRAR
                                                   DATOS
                                                        DE
                                                          PRODUCTOS
                                                          
                                                          
                                                          
                    1.Guardar un producto nuevo
                    2. eliminar un producto
                    3.Actualizar
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
            print(tabulate(GuardarProducto(),headers="keys",tablefmt="github"))
            input("precione una tecla para continuar ......")
                    
        if opcion == 2:
            idProducto = input("Ingrese el id del producto: ")
            print(tabulate(DeleteProducto(idProducto), headers="keys", tablefmt="github"))
            input("presione una tecla para continuar......")
            
            
        if opcion == 3:
            UP.menu()
            
            
        if opcion  == 0:
            break
        
       
            
            
        
            
            