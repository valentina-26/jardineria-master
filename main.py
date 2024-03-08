from tabulate import tabulate

import modules.getClients as clientes
import modules.getEmpleados as empleado
import modules.getOficina as oficina
import modules.getClients as cliente
import modules.getPedido as pedido
import modules.getPago as Pago
import sys



#print (tabulate(pedidos.getAllpedidosRechazados2009(), tablefmt = "rounded grid"))






if(__name__ == "__main__"):
    
  
    print(f"""
          
          
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
                                1.Cliente
                                2.Oficina
                                3.Empleado
                                4.Pedidos                                                   
                                                                    
                                                    
                                                   """)
    
    
opcion = opcion = int(input("seleccione una de las opciones: "))

if(opcion == 1):
    cliente.menu()
    
if(opcion == 2):
    oficina.menu()
    
if(opcion == 3):
    empleado.menu()
    
if(opcion == 4):
    pedido.menu()

    




