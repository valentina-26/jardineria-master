import storage.empleado as emp


#EJERCICIO 1
def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in em.empleados:
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
    
 #EJERCICIO 3   
    def getAllNombreApellidoPuesto(puesto):
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
            
            
            1.obtener todos los clientes(codigo y nombre)
            2.obtener u cliente por el codigo(codigo y nombre) 
            3.obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece(ejem: 3000 y .0 san francisco)
            4.obtener informacion segun el cogigo del empleado de ventas
            5.obtener clientes españoles
            
            
    """)
    
    opcion = opcion = int(input("seleccione una de las opciones: "))
            
            
            