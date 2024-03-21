import json
import requests
import os
import re
import modules.getPedido as Pe
from tabulate import tabulate
import modules.getClients as Gc
import modules.updatePedido as UPP

def guardarPedido():
    
    pedido = dict()
    while True:
        try:
            
            
            
            #CODIGO PEDIDO
            if not pedido.get("codigo_pedido"):
                codigo = input("Ingrese el codigo del pedido: ")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo = int(codigo)
                    asd = Pe.GETALLCODIGOPEDIDO(codigo)
                    if asd:
                        raise Exception("El codigo del pedido ya existe.")
                    else:
                        pedido["codigo_pedido"] = codigo
                else:
                    raise Exception("Codigo no valido, recuerde ingresar solo digitos numéricos")
            
        
            
            
            #FECHA PEDIDO
            if not pedido.get("fecha_pedido"):
                fecha_pedido = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pedido)is not None:
                    pedido["fecha_pedido"] = fecha_pedido
                else:
                    raise Exception("Fecha no valida, utilice el formato Año-mes-dia")

                    
            #FECHA ESPERADA
            if not pedido.get("fecha_esperada"):
                fecha_esperada = input("Ingrese la fecha estimada: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_esperada)is not None:
                    pedido["fecha_esperada"] = fecha_esperada
                else:
                    raise Exception("Fecha no valida, utilice el formato Año-mes-dia ")
            
                    
                    
            #FECHA ENTREGA
            if not pedido.get("fecha_entrega"):
                fecha_entrega = input("Ingrese la fecha de entrega: ")
                if fecha_entrega.strip().lower() == "none":
                    pedido["fecha_entrega"] = None
                elif re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_entrega)is not None:
                    pedido["fecha_entrega"] = fecha_entrega
                else:
                    raise Exception("Fecha no valida, utilice el formato Año-mes-dia")
                    
                    
            #ESTADO
            if not pedido.get("estado"):
                estado = input("Ingrese el estado del pedido: ")
                if re.match(r'^[A-Z][a-z]*$',estado)is not None:
                    asd = Pe.getAllEstdo(estado)
                    if asd:
                        pedido["estado"] = estado
                    else:
                        raise Exception("Opciones validas: Entregado / Rechazado / Pendiente ")
                else:
                    raise Exception("OPciones validas: Entregado / Rechazado / Pendiente ")
                
                   
            #COMENTARIO
            if not pedido.get("comentario"):
                comentario =input("ingrese el cometario del producto: ")
                if comentario.strip() == "":
                    pedido["comentario"] = comentario
                    
                    
            #CODIGO CLIENTE
            if not pedido.get("codigo_cliente"):
                codigo = input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo = int(codigo)
                    asd = Gc.getOneClienteCodigo(codigo)
                    if asd:
                        pedido["codigo_cliente"] = codigo
                        break
                    else:
                        raise Exception("El codigo del cliente no esta registrado.")
                else:
                    raise Exception("El codigo del cliente no esta registrado.")                 
            
        except Exception as error:
            print(error)
        
    
    peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado exitosamente"
    return [res]



def DeletePedido(id):
    data = Pe.DeletePEDIDO(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pedido eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Pedido no encontrado.",
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
                                                                       PEDIDO
                    
                
                    1.Guardar un pedido nuevo
                    2.Eliminar un pedido
                    3.Actualizar
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(guardarPedido(),headers="keys",tablefmt="github"))
                    input("precione una tecla para continuar ......")
                    
        elif opcion == 2:
                    idPedido = input("Ingrese el id del Pedido : ")
                    print(tabulate(DeletePedido(idPedido), headers="keys", tablefmt="github"))
                    
        elif opcion == 3:
            UPP.menu()
            
            
        elif (opcion == 0):
           break
       
     
            
            