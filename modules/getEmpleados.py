from tabulate import tabulate

import storage.empleado as emp



#EJERCICIO 3
def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in emp.empleados:
        if val.get("codigo_jefe") == codigo:
            NombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos":f'{val.get("apellido1")}{val.get("apellido2")}',
                    "email":val.get("email"),
                    "jefe":val.get("codigo_jefe")
                }
            )

    
 #EJERCICIO 2
def getAllPuestoNombreApellidoEmailJefe():
    PuestoNombreApellido = []   
    for val in emp.empleados:
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
    
 #EJERCICIO 2
    def getAllNombreApellidoPuesto():
        NombreApellidoPuesto =[]
        for val in emp.empleados:
            if val.get("puesto") != "Representante Ventas" :
            
                NombreApellidoPuesto.append({
                "nombre": val.get ("nombre"),
                "apellido1": val.get ("apellido1"),
                "puesto": val.get ("puesto"),
                "email": val.get ("email")
                
                })
        return NombreApellidoPuesto
            
            
def menu():
    

    print("""
          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                              
            
            1.obtener infromacion del jefe directo
            2.obtener informacion del director general
            3.obtener nombre, apellido y puesto de empleados que no sean representantes de ventas
            
           
            
            
    """)
    
    
    opcion = opcion = int(input("seleccione una de las opciones: "))
    
    
    
    if (opcion == 1):
        codigoJefe=int(input("Por favor ingrese el codigo del jefe:" ))
        print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))
        
    elif (opcion == 2):
        print(tabulate(getAllPuestoNombreApellidoEmailJefe(), headers="keys", tablefmt="github"))
    
    else:
        print(tabulate(getAllNombreApellidoPuesto(), headers="keys", tablefmt="github"))
        
        menu()
            
            
            
            