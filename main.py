import os
from tabulate import tabulate

import modules.getEmpleados as empleado
import modules.getOficina as oficina
import modules.getClients as cliente
import modules.getPedido as pedido
import modules.getProductos as productos
import modules.getPago as pago

productos.getAllData




print (tabulate(cliente.getAllclientesMadridRepre1138(), tablefmt = "rounded grid"))







if __name__ == "__main__":
    while True:
        print(f"""
     _  _ ____ __ _  _  _    ____ ____ __ __ _  ___ __ ____  __   __   
    ( \/ |  __|  ( \/ )( \  (  _ (  _ (  |  ( \/ __|  |  _ \/ _\ (  )  
    / \/ \) _)/    /) \/ (   ) __/)   /)(/    ( (__ )( ) __/    \/ (_/
    \_)(_(____)_)__)\____/  (__) (__\_|__)_)__)\___|__|__) \_/\_/\____/


                                    1.Cliente
                                    2.Oficina
                                    3.Empleado
                                    4.Pedidos
                                    5.productos
                                    6.pago
                                    0.salir                                                   
                                                                        
                                                        
                                                    """)
        
        opcion = int(input("seleccione una de las opciones: "))
        #print("Presiona [Ctrl + C] Para salir del programa...")
        
        # try:
        #     opcion = int(input("seleccione una de las opciones: "))
        # except KeyboardInterrupt:
        #     os.system("clear")
        #     print("Has salido exitosamente!")
        #     break
        # else:

        if(opcion == 1):
                cliente.menu()
                
        elif(opcion == 2):
                oficina.menu()
                
        elif(opcion == 3):
                empleado.menu()
                
        elif(opcion == 4):
                pedido.menu()
        
        elif(opcion == 5):
                productos.menu()
                
        elif(opcion == 6):
                pago.menu()
                
        elif(opcion == 0):
                break
                
        