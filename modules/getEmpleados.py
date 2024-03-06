import storage.empleado as emp



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
            
            
            