import json
import requests
from tabulate import tabulate
import os
import re
import modules.getEmpleados as gE

def GuardarEmpleado():
    empleado = dict ()
    while True:
        try:
            
            
            #CODIGO EMPLEADO
            if not empleado.get("codigo_empleado"):
                codigo = input("ingrese el codigo del empleado")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo_empleado = int(codigo)
                    GFGF = gE.getallempleCode(codigo)
                    if GFGF:
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        empleado["codigo_empleado"] = codigo_empleado
                else:
                    raise Exception(f"El codigo no cumple con el estandar establecido.")
                

            #NOMBRE
            if not empleado.get("nombre"):
                nombre = input("ingrese el nombre del empleado")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    empleado["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, por favor las palabras deben iniciar con mayúsculas.")
                
            
            #APELLIDO 1
            if not empleado.get("apellido1"):
                apellido1 = input("ingrese el primer apellido del empleado")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido1) is not None:
                    empleado["apellido1"] = apellido1
                else:
                    raise Exception("Apellido no valido, por favor todas las palabras deben iniciar con mayúsculas.")
                
            
            #APELLIDO2
            if not empleado.get("apellido2"):
                apellido2=input("ingrese el segundo apellido del empleado")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido2) is not None:
                    empleado["apellido2"] = apellido2
                else:
                    raise Exception("Apellido no valido, por favor todas las palabras deben iniciar con mayúsculas.")
                

            #EXTENSION
            if not empleado.get("extension"):
                extension = input(f"Ingrese la extension del empleado: ")
                if re.match(r'^\d{4}$', extension) is not None:
                    empleado["extension"] = extension
                else:
                    raise Exception("Extension no valida, por favor ingresar 4 dígitos numéricos.")
                
                
            
            #EMAIL    
            if not empleado.get("email"):
                email = input(f"Ingrese el email del empleado: ")
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', email) is not None:
                    empleado["email"] = email
                else:
                    raise Exception("Email no valido, por favor rectifique.")
                
                
            #CODIGO OFICINA    
            if not empleado.get("codigo_oficina"):
                codigo_oficina = input(f"Ingrese el codigo de la oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo_oficina) is not None:
                    empleado["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception("Codigo no valido, por favor rectificar")
                
                
            #CODIGO JEFE
            if not empleado.get("codigo_jefe"):
                codigo = input("Ingrese el codigo del jefe: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    empleado["codigo_jefe"] = codigo
                else:
                    raise Exception("El codigo del jefe no es valido, por favor rectifique.")
                
                
            #PUESTO
            if not empleado.get("puesto"):
                puesto = input(f"Ingrese el puesto del empleado: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', puesto) is not None:
                    vvv = gE.getallpuestoo(puesto)
                    if vvv:
                        empleado["puesto"] = puesto
                        break
                    else:
                        raise Exception("Puestos validos: ( Representante Ventas, Subdirector Marketing, Subdirector Ventas, Secretaria, Director Oficina )")
                else:
                    raise Exception("Puestos validos: ( Representante Ventas, Subdirector Marketing, Subdirector Ventas, Secretaria, Director Oficina )")



        except Exception as error:
            print(error)
    
                
            
            
    peticion = requests.get("http://172.16.103.34:5502",data=json.dumps(guardar, indent=4).encode("UTF-8"))
    res = peticion.json.json()
    res["mensaje"] = "Empleado guardado exitosamnete"
    return[res]



def DeleteEmpleado(id):
    data = gE.getcodigoEmpleado(id)
    if len(data):
        peticion = requests.delete("http://172.16.103.34:5502/empleados/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Empleado eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Empleado no encontrado.",
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
                                            EMPLEADOS                  
                
                    1.Guardar un producto nuevo
                    2.Eliminar empleado
                    0.regresar al menu principal  
                
                    
                
            """)

                
        opcion = int(input("seleccione una de las opciones: "))
                
        if (opcion == 1):
                    print(tabulate(GuardarEmpleado(),headers="keys",tablefmt="github"))
                    input("Precione una tecla para continuar ......")
                    
        if (opcion == 2):
            idEmpleado = int(input("Ingrese el id del Empleado: "))
            print(tabulate(DeleteEmpleado(idEmpleado), headers="keys", tablefmt="github"))
            input("precione una tecla para continuar........")

        elif (opcion == 0):
            break
            