import os
import json
import re
from tabulate import tabulate 
import requests
import modules.getClients as gC


def guardarCliente():

    cliente = dict()
    while True:
        try:
            
            #CODIGO CLIENTE
            
            if not cliente.get("codigo_cliente"):
                codigo = input("ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    if gC.getOneClienteCodigo(codigo):
                        raise Exception("el codio del cliente ya existe")
                    else:
                        cliente["codigo_cliente"] = codigo
                else:
                    raise Exception ("el codigo ingresado no es valido,por favor ingrese solo digitos numericos")
                    
            
             #NOMBRE CLIENTE
             
            if not cliente.get("nombre_cliente"):
               nombre_cliente = input(f"Ingrese el nombre del cliente: ")
               if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre_cliente) is not None:
                    cliente["nombre_cliente"] = nombre_cliente
               else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
            
            #NOMBRE CONTACTO
            
            if not cliente.get("nombre_contacto"):
                nombre_contacto= input("ingrese el nombre del contacto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',nombre_contacto) is not None:
                    cliente["nombre_contacto"]= nombre_contacto
                else:
                    raise Exception("el nombre no es valido,por favor inicie todas las palabras con mayuscula")
             
            #APELLIDO CONTACTO
            
            if not cliente.get("apelllido_contacto"):
                apelllido_contacto = input("ingrese el apellido  del contacto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',apelllido_contacto) is not None:
                    cliente["apelllido_contacto"]= apelllido_contacto
                else:
                    raise Exception("el apellido ingresado no es valido,por favor inicie todas las palabras con mayuscula")
            
               
            # TELEFONO 
            
            if not cliente.get("telefono"):
                telefono= input("ingrese el numero de telefono: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$',telefono) is not None:
                    if gC.getAllTelefono(telefono):
                         raise Exception("el telefono ingresado ya existe")
                    else:
                        cliente["telefono"] = telefono
                else:
                    raise Exception ("Telefono no valido, ejm: 845210369 o 5 5487-8745 ")
                
            #FAX
            
            if not cliente.get("fax"):
                fax = input("ingrese el fax : ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$',fax) is not None:
                    cliente["fax"]= fax
                else:
                    raise Exception("el fax ingresado no es valido")
                
            #LINEA DIRECCION 1
            
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input("ingrese  la linea_direccion1 : ")
                cliente["linea_direccion1"]= linea_direccion1
              
              
            #LINEA DIRECCION 2
            
            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input("ingrese  la linea_direccion2 : ")
                cliente["linea_direccion2"]= linea_direccion2
                
            
            #CIUDAD
            
            if not cliente.get("ciudad"):
                ciudad = input("ingrese la ciudad: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',ciudad) is not None:
                    cliente["ciudad"]= ciudad
                else:
                    raise Exception("la ciudad ingresada no es valida")
                
            #REGION
            
            if not cliente.get("region"):
                region= input("ingrese la region: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',region) is not None:
                    cliente["region"]= region
                else:
                    raise Exception("la region ingresada no es valida")
                
            #PAIS
            
            if not cliente.get("pais"):
                pais= input("ingrese  el pais: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',pais) is not None:
                    cliente["pais"]= pais
                else:
                    raise Exception("el pais ingresado no es valido")
                
            #CODIGO POSTAL
            
            if not cliente.get("codigo_postal"):
                codigo_postal = input("Ingrese el Codigo postal: ")
                if re.match(r'^\d{4,5}$', codigo_postal) is not None:
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception("Codigo postal no valido, asegurese de ingresar 4 o 5 dígitos numéricos")
            
            
            #CODIGO EMPLEADO REP VENTAS
        
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigo_empleado_rep_ventas = input(f"Escriba el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigo_empleado_rep_ventas) is not None:
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception("Codigo ingresado no valido,por favor ingresar solo dígitos numéricos")
            
            
            #LIMITE CREDITO
                
            if not cliente.get("limite_credito"):
                limite_credito = input(f"Escriba el limite de credito: ")
                if re.match(r'^[0-9]+$', limite_credito) is not None:
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception("Limite de credito  no valido, por favor ingresar solo dígitos numéricos")
                                   
        except Exception as error:
            print(error)

    peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado exitosamente"
    return [res]  

 

def DeleteClientes(id):
    data = gC.DeleteCliente(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Cliente no encontrado.",
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
                                            CLIENTES
                
                    1.Guardar un cliente nuevo
                    2.Eliminar
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(guardarCliente(),headers="keys",tablefmt="github"))
                    input("precione una tecla para continuar ......")
                    
                    
        elif opcion == 2:
                idCliente = input("Ingrese el id del cliente: ")
                print(tabulate(DeleteClientes(idCliente), headers="keys", tablefmt="github"))
                input("precione una tecla para continuar ......")
        elif (opcion == 0):
            break
            
            
            
            
               