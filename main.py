#print (tabulate(cliente.getAllclientesMadridRepre1138(), tablefmt = "rounded grid"))
import os
from tabulate import tabulate
import os
import modules.getEmpleados as empleado
import modules.getOficina as oficina
import modules.getClients as cliente
import modules.getPedido as pedido
import modules.getProductos as productos
import modules.getPago as pago
import modules.postProducto as CRUDproducto
import modules.getProductos as Repproducto


def menuProducto():
       while True:
        os.system("clear")
        print("""
 ___  __  ___  _  _  _  _  ___  _  _  __  ___    __      __   __      __  __  ___  _  _  _  _   
(  ,)(  )(  _)( \( )( )( )(  _)( \( )(  )(   \  /  \    (  ) (  )    (  \/  )(  _)( \( )( )( )  
 ) ,\ )(  ) _) )  (  \\//  ) _) )  (  )(  ) ) )( () )   /__\  )(__    )    (  ) _) )  (  )()(   
(___/(__)(___)(_)\_) (__) (___)(_)\_)(__)(___/  \__/   (_)(_)(____)  (_/\/\_)(___)(_)\_) \__/   
 ___  ___    ___  ___   __  ___  _  _  __  ____  __   ___                                       
(   \(  _)  (  ,\(  ,) /  \(   \( )( )/ _)(_  _)/  \ / __)                                      
 ) ) )) _)   ) _/ )  \( () )) ) ))()(( (_   )( ( () )\__ \                                      
(___/(___)  (_)  (_)\_)\__/(___/ \__/ \__) (__) \__/ (___/           
             
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
                       """)
               
        opcion = int(input("\nSelecione una de las opciones: "))

        if (opcion == 1):
                        Repproducto.menu()
        if (opcion == 2):
                        CRUDproducto

        if (opcion == 0):
                        break





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
                                    0.salir                                                   
                                                                        
                                                        
                                                    """)
        
        opcion = int(input("seleccione una de las opciones: "))
       

        if(opcion == 1):
                        cliente.menu()
                        
        elif(opcion == 2):
                        oficina.menu()
                        
        elif(opcion == 3):
                        empleado.menu()
                        
        elif(opcion == 4):
                        pedido.menu()
                
        elif(opcion == 5):
                        productos.menu()#
                        
        elif(opcion == 6):
                        pago.menu()
                        
        elif(opcion == 0):
                        break
                        
        