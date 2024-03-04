import storage.cliente as cli

def search():
    clienteName=list()
    for val in cli.clientes:
        CodName=dict({
        
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
        clienteName.append(CodName)
        return clienteName
    
def getOneClienteCodigo(codigo):
    for i,val in cli.clientes:
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
    
def getAllClientPaisRegionCiudad(pais,region=None,ciudad=None):
    clienteZone = list()
    for val in cli.clientes:
        if(
            val.get('pais')== pais or
            (val.get('region')== region or val.get('region')==None) and
            (val.get('ciudad')== ciudad or val.get('ciudad')==None) 
        ):
            clienteZone.append(val)
    return clienteZone 