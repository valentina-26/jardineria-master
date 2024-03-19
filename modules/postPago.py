import json
import requests
from tabulate import tabulate
import os
import modules.getClients as gC
import re
import modules.getPago as Gp


def GuardarPago():
    
    pago = dict
    while True:
        try:
            
            #CODIGO CLIENTE
            
            if not pago.get("codigo_cliente"):
                codigo_cliente = input("ingrese el codigo del cliente")
                if re.match(r'^[0-9]+$', codigo_cliente) is not None:
                    codigo_cliente =int(codigo_cliente)
                    adios= gC.getOneClienteCodigo(codigo_cliente)
                    if adios:
                        pago["codigo_cliente"] = codigo_cliente
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido,por favor ingresar solo sigitos numericos")

            
            # FORMA PAGO
            if not pago.get("forma_pago"):
                forma_pago = input("ingrese la forma de pago")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', forma_pago) is not None:
                    holi =Gp.getAllformapago(forma_pago)
                    if holi:
                        pago["forma_pago"] = forma_pago
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido,por favor ingresar solo sigitos numericos")
            
           
            # ID TRANSACCION
            
            if not pago.get("id_transaccion"):
                id_transaccion = input("Ingrear el ID de transaccion: ")
                if re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id_transaccion) is not None:
                    Nose = Gp.getAllIDTransac(id_transaccion)
                    if Nose:
                        raise Exception("El ID de transaccion ya existe.")
                    else:
                        pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception("ID no valido, porfavor rectificar")
                
            # FECHA PAGO

            if not pago.get("fecha_pago"):
                fecha_pago = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None:
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception("Fecha ingresada no valida,por favor utilice el formato (Año/mes-/dia)")


            # PAGO
            
            if not pago.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^[0-9]+$', total) is not None:
                    total = int(total)
                    pago["total"] = total
                    break
                else:
                    raise Exception("Total por favor ingresar solo digitos numericos.")

        except Exception as error:
            print(error)


    peticion = requests.get("http://172.16.103.34:5505",data=json.dumps(GuardarPago, indent=4).encode("UTF-8"))
    res = peticion.json.json()
    res["mensaje"] = "Pago guardado exitosamnete"
    return[res]



def DeletePago(id):
    data = Gp.GETpagocodigo(id)
    if len(data):
        peticion = requests.delete("http://172.16.103.34:5505/pagos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pago eliminado exitosamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Pago no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }





def menu():
    while True:
        print("""
                        ADMINISTRAR
                                    DATOS
                                           DE
                                              PAGO                                                         
                
                    1.Guardar un producto nuevo
                    2.eliminar pago
                    0.regresar al menu principal  
                
                    
                
            """)
        
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(GuardarPago(),headers="keys",tablefmt="github"))
                    input("precione una tecla para continuar ......")
                    
                    
                    
        if (opcion == 2):
            idPago = int(input("Ingrese el id del pago: "))
            print(tabulate(DeletePago(idPago), headers="keys", tablefmt="github"))
            input("precione una tecla para continuar .....")
            

        elif (opcion == 0):
            break