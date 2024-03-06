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
       if(val.get("codigo_cliente")==):
           codigo_cliente.append(val)
    return codigo_cliente


def getAllcomentario(codigoproducto):
    comentario=[] 
    for val in ped.pedido:
       if(val.get("comentario")==None):
           comentario.append(val)
    return comentario



def getAllEstadopedido(entregado,rechazado,pendiente):
    EstadoCliente = [] 
    for val in ped.pedido:
        
        if(val.get('estado') == entragado):
           (val.get('estado')== rechazado)
           (val.get ('estado')== pendiente)
        EstadoCliente.append
        
    return EstadoCliente
        
        
        
        
        