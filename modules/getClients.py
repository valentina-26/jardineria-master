
from tabulate import tabulate
import requests
import os
import modules.getEmpleados as emp

def getAllEMPLEADO():
     peticion = requests.get("http://154.38.171.54:5003/empleados")
     data = peticion.json()
     return data

def getAllCLIENTE():
     peticion = requests.get("http://154.38.171.54:5001/cliente")
     data = peticion.json()
     return data
 
 
def getcodigoClientee(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{codigo}")
    return [peticion.json()] if peticion.ok else []


def DeleteClienteaaa(id):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{id}")
    return [peticion.json()] if peticion.ok else []


def getClienteCodigoOTRO(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente?codigo_cliente={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data




def getAllTelefono(telefono):
    for val in getAllCLIENTE():
        if val.get("telefono") == telefono:
            return [val]


#EJERCICIO 1
def getAllClientName():
    clienteName=list()
    for val in getAllCLIENTE():
        CodigoName=dict({
        
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
        clienteName.append(CodigoName)
    return clienteName


#EJERCICIO 2    
def getOneClienteCodigo(codigo):
    clienteName=list()
    for val in getAllCLIENTE():
        if(val.get("codigo_cliente")==codigo):
            return({
                    
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
                    
                    })
    return clienteName       
 
#EJERCICIO 3                
def getAllClientsCreditCiudad(limiteCredit, ciudad):
    ClienteCredito = list()
    for val in getAllCLIENTE():
        if(val.get("limite_credito")>=limiteCredit and val.get("ciudad")==ciudad):
            ClienteCredito.append({
                "Codigo": val.get('codigo_cliente'),
                "Responable":val.get('nombre_cliente'),
                "Director":f"{val.get('nombre_contacto')} {val.get('nombre-contacto')}",
                "Telefono":val.get('telefono'),
                "Fax":val.get('fax'),
                "Direcciones":f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen":f"{val.get('pais')} {val.get('region')}{val.get('ciudad')}{val.get('codigo_postal')}",
                "Codigo del asesor":{val.get('codigo_empleado_rep_ventas')},
                "Credito":val.get('limite_credito')
                })
    return ClienteCredito 
    


def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in getAllCLIENTE():

        if (val.get('pais') == pais):

            if (val.get('region') == region) or region == None:

                if (val.get('ciudad') == ciudad) or ciudad == None:

                    userInZone = {
                        "pais": val.get('pais'),
                        "ciudad": val.get('ciudad'),
                        "region": val.get('region')
                    }
                    clientZone.append(userInZone)

    return clientZone



#EJERCICIO 4
def getAllClientsCodigoEmpleadoRepVentas(codigo):
    codigo_empleado = list()
    for val in getAllCLIENTE():
        if (val.get("codigo_empleado_rep_ventas")==codigo):
           codigo_empleado.append(val)
    return codigo_empleado



def getAllCLientCreditCiudad(limitCredit, ciudad) :
    clienteCredic= list()
    for val in getAllCLIENTE():
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad) :
            clienteCredic.append(val)
    return clienteCredic


# EJERCICIO 5
def getAllclientesEspañoles():
    clientesEspañoles = []
    for val in getAllCLIENTE():
        if(val.get("pais") == "Spain"):
        
            clientesEspañoles.append (val)
        
    return clientesEspañoles 

#EJERCICIO 6
def getAllclientesMadridRepre1138():
    MadridYCodigoRepresentante = list()
    for val in getAllCLIENTE():
        if val.get("ciudad") == "Madrid" and ((val.get("codigo_empleado_rep_ventas") == 11 or val.get("codigo_empleado_rep_ventas") == 30)):
                MadridYCodigoRepresentante.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
                })
    return MadridYCodigoRepresentante

#EJERCICIO 7
def getAllnombreCliapellidoRepre():
    NombreApell=[]
    for val in getAllCLIENTE():
        for cast in getAllEMPLEADO():
            if val.get("codigo_empleado_rep_ventas") == cast.get("codigo_empleado"):
                NombreApell.append({
                    "Nombre Cliente": val.get("nombre_cliente"),
                    "Representante de ventas": (f' {cast.get("apellido1")}')
                })
    return NombreApell
                


#EJERCICIO 8


    
    
    
    
    


def menu():

    while True:
        print(f"""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____     ___ __   __ ____ __ _ ____ ____ ____ 
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)   / __|  ) (  |  __|  ( (_  _|  __) ___)
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)   ( (__/ (_/\)( ) _)/    / )(  ) _)\___ \
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)   \___)____(__|____)_)__)(__)(____|____/
            
            
            0.Regresar
            1.obtener todos los clientes(codigo y nombre)
            2.obtener cliente por el codigo(codigo y nombre) 
            3.obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece(ejem: 3000 y .0 san francisco)
            4.obtener informacion segun el cogigo del empleado de ventas
            5.obtener clientes españoles
            6.obtener listado de todos los cliente de la ciudad de madrid y cuyo representante de ventas tenga el codigo de empleado 11 o 38
            7.obtener nombre de cada cliente y apellido de su representante de ventas
            
            
    """)
    
        opcion = int(input("seleccione una de las opciones: "))
            
            
        if (opcion == 1):
                print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
                
        elif(opcion == 2):
        
                codigoCliente = int(input("ingrese el codigo del cliente: "))
                print(tabulate(getOneClienteCodigo(codigoCliente), headers="keys", tablefmt="github"))
                
        
        elif(opcion == 3):
            limite = float(input("ingrese el limite credito de los clientes que desa visualizar: "))
            ciudad =input("ingrese el nombre de la ciudad que deseas filtar  de los clientes: ") 
            print(tabulate(getAllClientsCreditCiudad(limite, ciudad), headers="keys", tablefmt="github"))
            input("presione una tecla par continar......")
                
            
        elif (opcion == 4):
                codigoEmpleado=int(input("ingrese el codigo del empleado "))
                print(tabulate(getAllClientsCodigoEmpleadoRepVentas(codigoEmpleado),headers="keys", tablefmt="github"))
                
        elif (opcion == 5):
            print(tabulate(getAllclientesEspañoles(),headers="keys", tablefmt="github"))
            input("presione una teclapara continuar.....")
                
        
        elif (opcion == 6):
                print(tabulate(getAllclientesMadridRepre1138(), headers="keys", tablefmt="github"))     
                
        elif (opcion == 7):
            print(tabulate(getAllnombreCliapellidoRepre(),headers="keys", tablefmt="github"))
            input("presione una tacla para continuar.....")
    
            
        elif(opcion == 0):
            break
                
        
    
        
        
          
          
       
       
       
       
       

       


    


    
    
    

