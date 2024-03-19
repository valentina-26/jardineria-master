import requests

def getAllGAMA():
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = list()
    for val in getAllGAMA():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
     

#     def menu():
#     while True:
#         print("""
          
#  ____ ____ ____  __ ____ ____ ____    ____ ____    ____ _  _ ____ __   ____  __  ____  __  ____ 
# (  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  __| \/ |  _ (  ) (  __)/ _\(    \/  \/ ___)
#  )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) _)/ \/ \) __/ (_/\) _)/    \) D (  O )___ /
# (__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (____)_)(_(__) \____(____)_/\_(____/\__/(____/

#             0.Regresar
#             1.obtener informacion del jefe directo
            
#             """)
    
    
#         opcion = int(input(" "))
        
        
        
        # if (opcion == 1):
        #     codigoJefe=int(input("Por favor ingrese el codigo del jefe:" ))
        #     print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))