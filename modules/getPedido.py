from tabulate import tabulate
import requests
from datetime import datetime

def getAllPEDIDO():
     peticion = requests.get("http://154.38.171.54:5007/pedidos")
     data = peticion.json()
     return data
 
 
def getPedidoCodigoasd(codigo):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos/{codigo}")
    return [peticion.json()] if peticion.ok else []
 
def DeletePEDIDO(id):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos/{id}")
    return [peticion.json()] if peticion.ok else []
 
 
 
def getPedidoCodigoOTRO(codigo):
    peticion = requests.get(f"http://154.38.171.54:5007/pedidos?codigo_pedido={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data
 
 
 
def getAllEstdo(estado):
    for val in getAllPEDIDO():
        if val.get("estado") == estado:
            return [val] 
 
 
def GETALLCODIGOPEDIDO(codigo):
    for val in getAllPEDIDO():
        if(val.get("codigo_cliente") == codigo):
            return val
 
 
def getAllCodigoPedido(codigo):
    for val in  getAllPEDIDO():
        if(val.get("codigo_pedidio") == codigo):
            return val

#EJERCICIO 1
def getAllEstadoEntregado():
    estado_producto=[ ] 
    for val in getAllPEDIDO():
       if(val.get("estado") == "Entregado"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 2
def getAllEstadoRechazado():
    estado_producto=[ ] 
    for val in getAllPEDIDO():
       if(val.get("estado") == "Rechazado"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 3
def getAllEstadoPendiente():
    estado_producto=[ ] 
    for val in getAllPEDIDO():
       if(val.get("estado") == "Pendiente"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 4
def getAllcomentario():
    comentario=[] 
    for val in getAllPEDIDO():
       if(val.get("comentario")==None):
           comentario.append(val)
    return comentario






#EJERCICIO 5
def getAllpedidosEntregadosAtrasadosTiempo():
    pedidosEntregados=[]
    for val in getAllPEDIDO():
        
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
# EJERCICIO 10lif
                 
 #EJERCICIO 6           
def getAllcodigoPedidoCodigoClienteFecha():
    pedidoCodigoFecha=[]
    for val in getAllPEDIDO():
        
        if(val.get("estado")=="entregado") and val.get("fecha_de_entrega" == None):
            val.get["fecha_entrega"]  = val.get("fecha_esperada")
            
        if val.get("estado") == ("entregado"):
            date_1 = "/".join(val.get("fecha_entregada").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start =datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2,"%d/%m/%Y")
                
            diff = end.date() - start.date()
            if(diff.days >= 2):
                   pedidoCodigoFecha.append({
                       "codigo_de_pedido":val.get("codigo_pedido"),
                       "codigo_de_cliente":val.get("codigo_cliente"),
                       "fecha_esperada":val.get("fecha_esperada"),
                       "fecha_de_entrega":val.get("fecha_entrega")
                   })
    return pedidoCodigoFecha


#todos los pedidios rechazados en el 2009 EJERCICIO 11
#EJERCICIO 7


def getAllpedidosRechazados2009():
    pedidosRechazados2009 = []
    for val in getAllPEDIDO():
        fechaRechazo = val.get("fecha_esperada")
        if val.get("estado") == "Rechazado" and fechaRechazo.startswith("2009"):
            pedidosRechazados2009.append(val)
    return pedidosRechazados2009




#EJERCICIO 8
#lista pedidos entregados en enero de cualquier año EJERCICIO 12
def getAllPedidosEnero():
    PedidosEnero = list()
    for val in getAllPEDIDO():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                PedidosEnero.append(val)
    return PedidosEnero
         
         
         
def menu():
    while True:
        print("""
          
 ____ ____ ____  __ ____ ____ ____    ____ ____    ____ ____ ____ __ ____  __  
(  _ (  __|  _ \/  (  _ (_  _|  __)  (    (  __)  (  _ (  __|    (  |    \/  \ 
 )   /) _) ) __(  O )   / )(  ) _)    ) D () _)    ) __/) _) ) D ()( ) D (  O )
(__\_|____|__)  \__(__\_)(__)(____)  (____(____)  (__) (____|____(__|____/\__/ 
            
            
            
            0.Regresar
            1.obtener todos los pedidos con estado = entregado
            2.obtener todos los pedidos con estado = rechazado
            3.obtener todos los pedidos con estado = pendiente
            4.obtener lista de todos lo pedidos que no tienen comentarios
            5.obtener si un pedido fue entregado a tiempo o retrazado
            6.obtener todos los pedidos entregados 2 dias antes de la fecha de entrega
            7.obtener todos los pedidos rechazados en el 2009
            8.obtener lista de pedidos entregados en enero de cualquier año
           
            
           
            
            
    """)
    
    
        opcion = int(input("seleccione una de las opciones: "))
        
        if (opcion == 1):
            print(tabulate(getAllEstadoEntregado(), headers="keys", tablefmt="github"))
            
        
        elif (opcion == 2):
            print(tabulate(getAllEstadoPendiente(), headers="keys", tablefmt="github"))
            
        
        elif (opcion == 3):
            print(tabulate(getAllEstadoPendiente(), headers="keys", tablefmt="github"))
            
            
        elif (opcion == 4):
            print(tabulate(getAllcomentario(), headers="keys", tablefmt="github"))
            
            
        elif (opcion == 5):
            print(tabulate(getAllpedidosEntregadosAtrasadosTiempo(), headers="keys", tablefmt="github"))
            
            
        elif (opcion == 6):
            print(tabulate(getAllcodigoPedidoCodigoClienteFecha(), headers="keys", tablefmt="github"))
            
            
        elif (opcion == 7):
            print(tabulate(getAllpedidosRechazados2009(), headers="keys", tablefmt="github"))
            
            
        elif(opcion == 8):
            print(tabulate(getAllPedidosEnero(), headers="keys", tablefmt="github"))
            
        elif(opcion == 0):
            break