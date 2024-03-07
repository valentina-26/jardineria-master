import storage.pedido as ped


def getAllEstado(entrgado):
    estado_producto=[ ] 
    for val in ped.pedido:
       if(val.get("estado") == entrgado):
           estado_producto.append(val)
    return estado_producto


def getAllcodigocliente():
    codigo_cliente=[] 
    for val in ped.pedido:
       if(val.get("codigo_cliente")):
           codigo_cliente.append(val)
    return codigo_cliente


def getAllcomentario(codigoproducto):
    comentario=[] 
    for val in ped.pedido:
       if(val.get("comentario")==None):
           comentario.append(val)
    return comentario



def getAllEstadopedido(Entregado,rechazado,pendiente):
    EstadoCliente = [] 
    for val in ped.pedido:
        
        if(val.get('estado') == "Entragado"):
           (val.get('estado')== "rechazado")
           (val.get ('estado')== "pendiente")
        EstadoCliente.append(val)
        
    return EstadoCliente

from datetime import datetime

def getAllpedidosEntregadosAtrasadosTiempo():
    pedidosEntregados=[]
    for val in ped.pedido:
        
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
                date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
                date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
                start = datetime.strptime(date_1,"%d/%m/%Y")
                end = datetime.strptime(date_2,"%d/%m/%Y")
                
                diff = end.date() - start.date()
                if(diff.days < 0):
                   pedidosEntregados.append({
                       "codigo_de_pedido":val.get("codigo_pedido"),
                       "codigo_de_cliente":val.get("codigo_cliente"),
                       "fecha_esperada":val.get("fecha_esperada"),
                       "fecha_de_entrega":val.get("fecha_entrega")
                   })
    return pedidosEntregados       

#listado con el codigo pedido
#codig cliente
#fecha esperada
#y fecha de entrega de pedidos entrgados 2 dias antes de la fecha esperada
                 
            
def getAllcodigoPedidoCodigoClienteFecha():
    pedidoCodigoFecha=[]
    for val in ped.pedido:
        
        if(val.get("estado")=="entregado") and val.get("fecha_de_entrega" == None):
            val.get["fecha_entrega"]  = val.get("fecha_esperada")
            
        if val.get("estado") == ("entregado"):
            date_1 = "/".join(val.get("fecha_entregada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime()
            end = datetime.strptime(date_2,"%d/%m/%Y")
                
            diff = end.date() - start.date()
            if(diff.days >=2):
                   pedidoCodigoFecha.append({
                       "codigo_de_pedido":val.get("codigo_pedido"),
                       "codigo_de_cliente":val.get("codigo_cliente"),
                       "fecha_esperada":val.get("fecha_esperada"),
                       "fecha_de_entrega":val.get("fecha_entrega")
                   })
    return pedidoCodigoFecha


#todos los pedidios rechazados en el 2009

def getAllpedidosRechazados2009():
    pedidosRechazados= []
    for val in ped.pedido:
        fechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        start = datetime.strptime(fechaPedido,"%d/%m/%Y") 
        
        if val.get("estado") == "Rechazado" and start.year == 2009:
        
              pedidosRechazados.append(val)
    return pedidosRechazados 


#lista pedidos entregados en enero de cualquier año EJERCICIO 12
def getAllPedidosEnero():
    PedidosEnero = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                PedidosEnero.append(val)
    return PedidosEnero
         
         
           
    






                  
            







      
        
        
        
        