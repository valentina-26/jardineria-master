import json
import requests
from tabulate import tabulate
import os
import modules.getClients as gC
import re
import modules.getPago as Gp


def GuardarPago():
    
    pago = dict ()
    while True:
        try:
            
            #CODIGO CLIENTE
            
            if not pago.get("codigo_cliente"):
                codigo =  input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo =int(codigo)
                    adios = gC.getOneClienteCodigo(codigo)
                    if adios:
                        pago["codigo_cliente"] = codigo
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido, por favor ingresar solo digitos numéricos.")

            
            # FORMA PAGO
            if not pago.get("forma_pago"):
                forma_pago = input("Ingrese el metodo de pago: ")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', forma_pago) is not None:
                    mmmmm = Gp.getAllformapago(forma_pago)
                    if mmmmm:
                        pago["forma_pago"] = forma_pago
                    else:
                        raise Exception("Formas de pago validas:PayPal / Transferencia / Cheque ")
                else:
                    raise Exception("Formas de pago validas:PayPal / Transferencia / Cheque ")
            
           
            # ID TRANSACCION
            
            if not pago.get("id_transaccion"):
                id_transaccion = input("Ingrese el ID de transaccion: ")
                if re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id_transaccion) is not None:
                    sss = Gp.getAllIDTransac(id_transaccion)
                    if sss:
                        raise Exception("El ID de transaccion ya existe.")
                    else:
                        pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception("ID no valido, sigue el formato ejm: ak-std-000026 ")
                
            # FECHA PAGO

            if not pago.get("fecha_pago"):
                fecha_pago = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None:
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception("Fecha no valida,utilice Año-mes-dia")


            # PAGO
            
            if not pago.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^[0-9]+$', total) is not None:
                    total = int(total)
                    pago["total"] = total
                    break
                else:
                    raise Exception("Total no valido, por favor solo digitos numericos.")

        except Exception as error:
            print(error)


    peticion = requests.post("http://154.38.171.54:5006/pagos", data=json.dumps(pago, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado exitosamente"
    return [res]


def DeletePago(id):
    data = Gp.DeletePagoaaaaaa(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
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
                                              PAGO                                                         
                
                    1.Guardar un pAGO nuevo
                    2.eliminar pago
                    0.regresar al menu principal  
                
                    
                
            """)
        
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                print(tabulate(GuardarPago(),headers="keys",tablefmt="github"))
                input("precione una tecla para continuar ......")
                    
                    
                    
        elif opcion == 2:
            pagoid = input("Ingrese el id del Pedido: ")
            print(tabulate(DeletePago(pagoid), headers="keys", tablefmt="github"))
            input("precione una tecla para continuar ......")
            

        if (opcion == 0):
            break