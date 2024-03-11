from tabulate import tabulate

from datetime import datetime

import storage.pago as pag


def getAllPagos2008():
    Pagos2008SinRepetir = list()
    PagosRepetidos = set()
    for val in pag.pago:
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
    for val in pag.pago:
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
    for val in pag.pago:
        val.get("forma_pago")
        formadepago.append(val.get("forma_pago"))
        convertir = set(str(item)for item in formadepago)
     
    return convertir 




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
            2.obtener listado con todas las formas de pago
            
           
            
            
    """)
    
        
        opcion = int(input("seleccione una de las opciones: "))

        if (opcion==1):
            print(tabulate(getAllPagos2008(), headers="keys", tablefmt="github"))

            
        elif (opcion == 2):
                print(tabulate(getAllPagosFecha(), headers="keys", tablefmt="github"))
                
                
        elif (opcion == 3):
                print(tabulate(getAllFormasPago(), headers="keys", tablefmt="github"))
                
        elif (opcion == 0):
            break




   
    
    
    
    
    