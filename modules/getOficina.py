
from tabulate import tabulate
import requests

def getAllOFICINA():
     peticion = requests.get("http://154.38.171.54:5005/oficinas")
     data = peticion.json()
     return data
 
 
def getCodigosOficiina(codigo):
    peticion = requests.get("http://154.38.171.54:5005/oficinas/{codigo}")
    return [peticion.json()] if peticion.ok else []
 
 
 
def GETCodigoOficina(codigo):
    for val in getAllOFICINA():
        if val.get("codigo_oficina") == codigo:
            return [val]



def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllOFICINA():
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllOFICINA():
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono


def menu():
    while True:
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____     __ ____ __ ___ __ __ _  __  
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)   /  (  __|  ) __|  |  ( \/ _\ 
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)   (  O ) _) )( (__ )(/    /    \
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)   \__(__) (__)___|__)_)__)_/\_/
            
            0.Regreasar
            1.obtener icodigo y ciudad de la oficina
            2.obtener informacion degun el pais
            
           
            
            
    """)
    
    
        opcion = int(input("seleccione una de las opciones: "))
        
        if (opcion == 1):
        
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
            
        elif (opcion == 2):
            pais = input("ingrese el pais: ")
            print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))
            
        elif (opcion == 0):
            break