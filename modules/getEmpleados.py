from tabulate import tabulate
import requests


def getAllEMPLEADO():
     peticion = requests.get("http://154.38.171.54:5003/empleados")
     data = peticion.json()
     return data
 
 
 
def getcodigoEmpleado(codigo):
    peticion = requests.get("http://154.38.171.54:5003/empleados/{codigo}")
    return [peticion.json()] if peticion.ok else []




def getallempleCode(codigo):
    for val in getAllEMPLEADO():
        if val.get("codigo_empleado") == codigo:
            return [val]



def getallpuestoo(puesto):
    for val in getAllEMPLEADO():
        if val.get("puesto") == puesto:
            return [val]




#EJERCICIO 1
def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in getAllEMPLEADO():
        if val.get("codigo_jefe") == codigo:
            NombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos":f'{val.get("apellido1")}{val.get("apellido2")}',
                    "email":val.get("email"),
                    "jefe":val.get("codigo_jefe")
                    
                    
                }
            )
    return NombreApellidoEmail
    
 #EJERCICIO 2
def getAllPuestoNombreApellidoEmailJefe():
    PuestoNombreApellido = []   
    for val in getAllEMPLEADO():
        if val.get("codigo_jefe") == None:
        
                PuestoNombreApellido.append(
                {
                    
                    "nombre": val.get ("nombre"),
                    "apellido1": val.get ("apellido1"),
                    "puesto": val.get ("puesto"),
                    "email": val.get ("email")
                
                }  
            )
                return PuestoNombreApellido          
    
 #EJERCICIO 3
def getAllNombreApellidoPuesto():
        NombreApellidoPuesto =[]
        for val in getAllEMPLEADO():
            if val.get("puesto") != "Representante Ventas" :
            
                NombreApellidoPuesto.append({
                "nombre": val.get ("nombre"),
                "apellido1": val.get ("apellido1"),
                "puesto": val.get ("puesto"),
                "email": val.get ("email")
                
                })
        return NombreApellidoPuesto
            
            
def menu():
    while True:
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____ _  _ ____ __   ____  __  ____  __  ____ 
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  __| \/ |  _ (  ) (  __)/ _\(    \/  \/ ___)
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) _)/ \/ \) __/ (_/\) _)/    \) D (  O )___ /
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (____)_)(_(__) \____(____)_/\_(____/\__/(____/

            0.Regresar
            1.obtener informacion del jefe directo
            2.obtener informacion del director general
            3.obtener nombre, apellido y puesto de empleados que no sean representantes de ventas
            
           
            
            
    """)
    
    
        opcion = int(input("seleccione una de las opciones: "))
        
        
        
        if (opcion == 1):
            codigoJefe=int(input("Por favor ingrese el codigo del jefe:" ))
            print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))
            
        elif (opcion == 2):
            print(tabulate(getAllPuestoNombreApellidoEmailJefe(), headers="keys", tablefmt="github"))
        
        elif (opcion == 3):
            print(tabulate(getAllNombreApellidoPuesto(), headers="keys", tablefmt="github"))
            
        elif(opcion == 0):
            break
            
        

    
        
            
            
            
            