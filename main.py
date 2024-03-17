#print (tabulate(cliente.getAllclientesMadridRepre1138(), tablefmt = "rounded grid"))
import os
from tabulate import tabulate
import modules.getEmpleados as empleado
import modules.getOficina as oficina
import modules.getClients as cliente
import modules.getPedido as pedido
import modules.getPago as pago
import modules.menu as menu
import re




if __name__ == "__main__":
  
    while True:
        os.system("clear")
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
                                    7.Gama
                                    0.salir                                                   
                                                                        
                                                        
                                                    """)
        
        
        opcion = (input("seleccione una de las opciones: "))

        if(re.match(r'[1-9]+$', opcion)is not None ):
            opcion =int(opcion)
            if(opcion>=0 and opcion<=5):
       

                if(opcion == 1):
                                menu.menu.menuCLIENTE()
                                    
                elif(opcion == 2):
                                menu.menu.menuOFICINA()
                                    
                elif(opcion == 3):
                                menu.menu.menuEMPLEADO()
                                    
                elif(opcion == 4):
                                menu.menu.menuPEDIDIO()
                            
                elif(opcion == 5):
                                menu.menuPRODUCTO()
                                    
                elif(opcion == 6):
                                menu.menu.menuPAGO()

                elif(opcion == 7):
                                menu.menu.menuGAMA()
                                    
                elif(opcion == 0):
                                    break
              
                            
            