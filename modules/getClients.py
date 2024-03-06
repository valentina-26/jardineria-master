import storage.cliente as cli

def getAllClientName():
    clienteName=list()
    for val in cli.clientes:
        CodigoName=dict({
        
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
        clienteName.append(CodigoName)
        return clienteName
    
def getOneClienteCodigo(codigo):
    for val in cli.clientes:
        if(val.get("codigo_cliente")==codigo):
            return{
                    
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
                    
                    }
                
def getAllClientsCreditCiudad(limiteCredit, ciudad):
    ClienteCredito = list()
    for val in cli.clientes:
        if(val.get("limite_credito")>=limiteCredit and val.get("ciudad")==ciudad):
            ClienteCredito.append(val)
        return ClienteCredito 
    

    
def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.clientes:

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



    
def getAllClientsCodigoEmpleadoRepVentas(argumento):
    codigo_empleado = list()
    for val in cli.clientes:
       if (val.get("codigo_empleado_rep_ventas")==11):
           codigo_empleado.append(val)
    return codigo_empleado



def getAllCLientCreditCiudad(limitCredit, ciudad) :
    clienteCredic= list()
    for val in cli.clientes :
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad) :
            clienteCredic.append(val)
    return clienteCredic


def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = list()
    for val in cli.clientes :
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) or 
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ) :
            clientZone.append(val)
    return clientZone


def getAllclientesEspañoles(pais):
    clientesEspañoles = []
    for val in cli.clientes :
        if(val.get("pais") == "Spain"):
        
            clientesEspañoles.append ({
                "pais": val.get("pais")
            })
        
        return clientesEspañoles 
    
          
          
       
       
       
       
       

       


    


    
    
    

