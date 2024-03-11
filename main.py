from tabulate import tabulate

import modules.getEmpleados as empleado
import modules.getOficina as oficina
import modules.getClients as cliente
import modules.getPedido as pedido
import modules.getPago as Pago
import sys



#print (tabulate(pedidos.getAllpedidosRechazados2009(), tablefmt = "rounded grid"))







def menu():
  
         print(f"""
 _  _ ____ __ _  _  _    ____ ____ __ __ _  ___ __ ____  __   __   
( \/ |  __|  ( \/ )( \  (  _ (  _ (  |  ( \/ __|  |  _ \/ _\ (  )  
/ \/ \) _)/    /) \/ (   ) __/)   /)(/    ( (__ )( ) __/    \/ (_/\
\_)(_(____)_)__)\____/  (__) (__\_|__)_)__)\___|__|__) \_/\_/\____/


                                1.Cliente
                                2.Oficina
                                3.Empleado
                                4.Pedidos                                                   
                                                                    
                                                    
                                                   """)
    
    
opcion = int(input("seleccione una de las opciones: "))

if(opcion == 1):
    cliente.menu()
    
if(opcion == 2):
    oficina.menu()
    
if(opcion == 3):
    empleado.menu()
    
if(opcion == 4):
    pedido.menu()

    




