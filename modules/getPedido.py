from tabulate import tabulate


import storage.pedido as ped

#EJERCICIO 1
def getAllEstado(Entregado):
    estado_producto=[ ] 
    for val in ped.pedido:
       if(val.get("estado") == "Entregado"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 2
def getAllEstado(rechazado):
    estado_producto=[ ] 
    for val in ped.pedido:
       if(val.get("estado") == "Rechazado"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 3
def getAllEstado(Pendiente):
    estado_producto=[ ] 
    for val in ped.pedido:
       if(val.get("estado") == "Pendiente"):
           estado_producto.append(val)
    return estado_producto

#EJERCICIO 4
def getAllcomentario(codigo_pedido):
    comentario=[] 
    for val in ped.pedido:
       if(val.get("comentario")==None):
           comentario.append(val)
    return comentario




from datetime import datetime

#EJERCICIO 5
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
# EJERCICIO 10
                 
 #EJERCICIO 6           
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


#todos los pedidios rechazados en el 2009 EJERCICIO 11
#EJERCICIO 7
def getAllpedidosRechazados2009():
    pedidosRechazados= []
    for val in ped.pedido:
        fechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        start = datetime.strptime(fechaPedido,"%d/%m/%Y") 
        
        if val.get("estado") == "Rechazado" and start.year == 2009:
        
              pedidosRechazados.append(val)
    return pedidosRechazados 

#EJERCICIO 8
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
         
         
         
def menu():
    

    print("""
          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                              
            
            
            
            
            1.obtener todos los pedidos con estado = entregado
            2.obtener todos los pedidos con estado = rechazado
            3.obtener todos los pedidos con estado = pendiente
            4.obtener el comentario de un pedido segun el codigo del pedido
            5.obtener si un pedido fue entregado a tiempo o retrazado
            6.obtener todos los pedidos entregados 2 dias antes de la fecha de entrega
            7.obtener todos los pedidos rechazados en el 2009
            8.obtener lista de pedidos entregados en enero de cualquier año
           
            
           
            
            
    """)
    
    
    opcion = opcion = int(input("seleccione una de las opciones: "))
    
    if (opcion == 6):
        print(tabulate(getAllcodigoPedidoCodigoClienteFecha(), headers="keys", tablefmt="github"))
         
           
    






                  
            







      
menu()        
        
        
        