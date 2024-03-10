
from tabulate import tabulate

import storage.oficina as ofc


def getAllCodigoCiudad():
    codigoCiudad = []
    for val in ofc.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in ofc.oficina:
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono


def menu():

    print("""
          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                              
            
            1.obtener icodigo y ciudad de la oficina
            2.obtener pais, ciudad, telefono y oficinas
           
            
            
    """)
    
    
    opcion = opcion = int(input("seleccione una de las opciones: "))
    
    if (opcion == 1):
      
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
        
    else:
        print(tabulate(getAllCiudadTelefono(), headers="keys", tablefmt='github'))
        
        
    menu()
        
    