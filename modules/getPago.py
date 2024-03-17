from tabulate import tabulate
import requests
from datetime import datetime


def getAllPAGO():
     peticion = requests.get("http://172.16.103.34:5505")
     data = peticion.json()
     return data

def getAllCLIENTE():
     peticion = requests.get("http://172.16.103.34:5501")
     data = peticion.json()
     return data

def getAllEMPLEADO():
     peticion = requests.get("http://172.16.103.34:5502")
     data = peticion.json()
     return data


def getAllPagos2008():
    Pagos2008SinRepetir = list()
    PagosRepetidos = set()
    for val in getAllPAGO:
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            if val.get("codigo_cliente") not in PagosRepetidos:
                Pagos2008SinRepetir.append(val)
                PagosRepetidos.add(val.get("codigo_cliente"))
    return Pagos2008SinRepetir

     #listado con pagos 2008 mediante paypal(ordenar mayor a menor) EJERCICIO 13

def getAllPagosFecha():
    pagosFecha = []
    for val in getAllPAGO:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)

    return pagosFecha
  
  
  
    #TODAS LAS FORMAS DE PAGO EJERCICIO 14 
def getAllFormasPago():
    formadepago = []
    for val in getAllPAGO:
        val.get("forma_pago")
        formadepago.append(val.get("forma_pago"))
        convertir = set(str(item)for item in formadepago)
     
    return convertir 

#EJERCICIO 4
def getAllClientReprePago():
    conPago = []
    otra= set()
    for val in getAllCLIENTE:
        for cast in getAllEMPLEADO:
            for san in getAllPAGO:
                
                if (san.get("codigo_cliente") == val.get("codigo_cliente")) and (val.get("codigo_empleado_rep_ventas") == cast.get("codigo_empleado")):
                    if val.get("nombre_cliente"): conPago
                    conPago.append({
                             "Nombre Cliente": val.get("nombre_cliente"),
                        "Representante de ventas": f'{cast.get("nombre")} {cast.get("apellido1")}'
                    })
                    otra.add(val.get("nombre_cliente"))
    return conPago
                
                
                
#EJERCICIO 5
def getAllClientRepresinPago():
    SINPago = []
    otra= set()
    for val in getAllCLIENTE:
        for cast in getAllEMPLEADO:
            for san in getAllPAGO:
                
                if (san.get("codigo_cliente") != val.get("codigo_cliente")) and (val.get("codigo_empleado_rep_ventas") == cast.get("codigo_empleado")):
                  SINPago.append  ({
                     "Nombre Cliente": val.get("nombre_cliente"), 
                      "Representante de ventas": f'{cast.get("nombre")} {cast.get("apellido1")}'
                   })
    return SINPago              
                
               

        




def menu():
    while True:
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____  __   ___  __  
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  _ \/ _\ / __)/  \ 
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) __/    ( (_ (  O )
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (__) \_/\_/\___/\__/ 

            0.Regresar
            1.obtener lista de pagos realizados en el 2008
            2.obtener listado de pagos en el año 2008 por medio de paypal(ordenados de mayor a menor)
            3.obtener listado con todas las formas de pago
            4.obtener nombre de cada cliente que ha realizado pagos junto con el  nombre de su representante de ventas
            5.obtener nombre de los clientes que no han realizado pagos junto con el nombre de su RV
           
            
            
    """)
    
        
        opcion = int(input("seleccione una de las opciones: "))

        if (opcion==1):
            print(tabulate(getAllPagos2008(), headers="keys", tablefmt="github"))

            
        elif (opcion == 2):
                print(tabulate(getAllPagosFecha(), headers="keys", tablefmt="github"))
                
                
        elif (opcion == 3):
                print(tabulate(getAllFormasPago(), headers="keys", tablefmt="github"))
                
        elif (opcion == 4):
            print(tabulate(getAllClientReprePago(), headers="keys", tablefmt="github"))
                
        elif (opcion == 5):
             print(tabulate(getAllClientRepresinPago(), headers="keys", tablefmt="github"))
            
            
                    
        elif (opcion == 0):
            break




   
    
    
    
    
    