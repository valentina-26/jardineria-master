import storage.pedido as ped

def getAllEstado(codigoproducto):
    estado_producto=[ ] 
    for val in ped.pedido:
       if(val.get("estado")=="Pendiente"):
           estado_producto.append(val)
    return estado_producto


def getAllcodigocliente(codigoproducto):
    codigo_cliente=[] 
    for val in ped.pedido:
       if(val.get("codigo_cliente")==codigoproducto):
           codigo_cliente.append(val)
    return codigo_cliente


def getAllcomentario(codigoproducto):
    comentario=[] 
    for val in ped.pedido:
       if(val.get("comentario")==None):
           comentario.append(val)
    return comentario

