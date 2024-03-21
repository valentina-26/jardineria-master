import json
import requests
import modules.getEmpleados as getEmp
from tabulate import tabulate
import os



#NOMBRE
def NOMBREempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["nombre"] = input("ingrese el nuevo nombre del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            
        
#APELLIDO
def APELLIDOempladoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado en el que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["apellido1"] = input("Ingrese el nuevo apellido 1 del empleado")
                    
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            

#APELLIDO 2
def APELLIDO2empleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["apellido2"] = input("ingrese el nuevo apellido 2 del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")




#EXTENSION
def EXTENSIONempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["extension"] = input("ingrese la nueva extension del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            

#EMAIL
def EMAILempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["email"] = input("ingrese el nuevo email del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            

#CODIGO OFICINA
def CODOFempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["codigo_oficina"] = input("ingrese el nuevo codigo de oficina: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            

#CODIGO JEFE
def CODJEFEempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["codigo_jefe"] = int(input("ingrese el nuevo codigo de jefe: "))
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")
            
            
            
            

#PUESTO
def PUESTOempleadoUpdate(codigo):
    while True:
        if(codigo != None):
            empleado= getEmp.getEmpleadoCodigoOTRO((codigo))
            if (empleado):
                print(tabulate(empleado, headers="keys", tablefmt="github"))
                LALA=int(input("""
                    ¿Este es el empleado que desea actualizar ?
                            1. Si
                            2. No
                """))
                if(LALA):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    empleado[0]["puesto"] = input("ingrese el nuevo puesto del empleado: ")
                    peticion = requests.put(f'http://154.38.171.54:5003/empleados/{empleado[0].get("id")}', headers= headers, data= json.dumps(empleado[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el empleado {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del empleado")





def menu():
  while True:
    os.system("clear")
    print("""


                                 ACTUALIZAR
                                             EMPLEADOS              


                                 1. Nombre del empleado
                                 2. Apellido 1 del empleado
                                 3. Apellido 2 del empleado
                                 4. Extension del empleado
                                 5. Email del empleado
                                 6. Codigo de oficina del empleado
                                 7. Codigo de jefe del empleado
                                 8. Puesto del empleado
                                 
                                 0. Salir
""")

    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigoempleado = input(("Ingrese el codigo del empleado al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(NOMBREempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(APELLIDOempladoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(APELLIDO2empleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(EXTENSIONempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(EMAILempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(CODOFempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(CODJEFEempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(PUESTOempleadoUpdate(codigoempleado), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 8 ")
               
    except ValueError: 
         print("Caracteres incorrectos, elija una opcion del 0 al 8")
     


