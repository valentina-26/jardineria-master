import storage.pago as pag


#listado con pagos 2008 mediante paypal(ordenar mayor a menor) EJERCICIO 13
def getAllPagosPaypal():
    pagospaypal2008 = []
    for val in pag.pago:
        fechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        start = datetime.strptime(fechaPedido,"%d/%m/%Y") 
        
        if val.get("forma_pago") == "paypal" and start.year == 2008:
            pagospaypal2008.append(val)
    return pagospaypal2008       
    
   
    
    
    
    
    #ef getAllpedidosRechazados2009():
    #pedidosRechazados= []
    #for val in ped.pedido:
        #fechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        #start = datetime.strptime(fechaPedido,"%d/%m/%Y") 
        
        #if val.get("estado") == "Rechazado" and start.year == 2009:
        
              #pedidosRechazados.append(val)
    #return pedidosRechazados 
    
    
    
    
    
    #def getAllcodigoPedidoCodigoClienteFecha():
    #pedidoCodigoFecha=[]
    #for val in ped.pedido:
        
        #if(val.get("estado")=="entregado") and val.get("fecha_de_entrega" == None):
            #val.get["fecha_entrega"]  = val.get("fecha_esperada")
            
        #if val.get("estado") == ("entregado"):
            #date_1 = "/".join(val.get("fecha_entregada").split("-")[::-1])
            #date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            #start = datetime.strptime()
            #end = datetime.strptime(date_2,"%d/%m/%Y")
                
            #diff = end.date() - start.date()
            #if(diff.days >=2):
                   #pedidoCodigoFecha.append({
                       #"codigo_de_pedido":val.get("codigo_pedido"),
                       #"codigo_de_cliente":val.get("codigo_cliente"),
                       #fecha_esperada":val.get("fecha_esperada"),
                       #fecha_de_entrega":val.get("fecha_entrega")
                   #})
    #return pedidoCodigoFecha
     
     

