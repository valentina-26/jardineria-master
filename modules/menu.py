#json-server storage/productos.json -b 5500 
#& json-server storage/cliente.json -b 5501 
#& json-server storage/empleado.json -b 5502 
#& json-server storage/gama.json -b 5503 
#& json-server storage/oficina.json -b 5504
#& json-server storage/pago.json -b 5505 
#& json-server storage/pedido.json -b 5506


# cliente:  http://154.38.171.54:5001/cliente
# detalles: http://154.38.171.54:5002/detalle_pedido
# empleados: http://154.38.171.54:5003/empleados
# gama?producto: http://154.38.171.54:5004/gama
# oficina: http://154.38.171.54:5005/oficinas
# pago: http://154.38.171.54:5006/pagos
# pedido: http://154.38.171.54:5007/pedidos
# producto: http://154.38.171.54:5008/productos

import re
import modules.postProducto as CRUDproducto
import modules.getProductos as Repproducto
import modules.getClients as repCliente
import modules.postClients as CRUDcliente
import modules.getEmpleados as RepEmpleado
import modules.postEmpleados as CRUDempleado
import modules.getGama as Repgama
import modules.postGama as CRUDgama
import modules.getOficina as Repoficina
import modules.postOficina as CRUDoficina
import modules.getPago as Reppago
import modules.postPago as CRUDpago
import modules.getPedido as Reppedido
import modules.postPedido as CRUDpedido
import os


#MENU PRODUCTO

def menuPRODUCTO():
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
                     
              opcion = (input("\nSelecione una de las opciones: "))
              
              if(re.match(r'[1-9]+$', opcion)is not None ):
                                   opcion =int(opcion)
                                   if(opcion>=0 and opcion<=5):
                     

                                          if (opcion == 1):
                                                 Repproducto.menu()
                                          if (opcion == 2):
                                                 CRUDproducto.menu()

                                          if (opcion == 0):
                                                 break


#MENU CLIENTES
                                   
def menuCLIENTE():
       while True:
        os.system("clear")
        print("""
                                  BIENVENIDO
                                            AL
                                              MENU
                                                   DE
                                                      CLIENTES                                                                                                                                                                                   
                                                                                                                              
             
                   1.Repotar los clientes
                   2.Guardar actualizar y eliminar clientes
                   0.regresar al menu principal 
                       """)
               
        opcion = (input("\nSelecione una de las opciones: "))
        
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                          repCliente.menu()
                                   if (opcion == 2):
                                          CRUDcliente.menu()

                                   if (opcion == 0):
                                          break

#MENU DE EMPLEADOS
                                   
def menuEMPLEADO():
       while True:
        os.system("clear")
        print("""
 ___ __ ___ _  _ _  _ ___ _  _ __ ___   __      __  __      __  __ ___ _  _ _  _    ___ ___ 
(  ,|  |  _| \( | )( |  _| \( |  |   \ /  \    (  )(  )    (  \/  |  _| \( | )( )  (   (  _)
 ) ,\)( ) _))  ( \\// ) _))  ( )( ) ) | () )   /__\ )(__    )    ( ) _))  ( )()(    ) ) ) _)
(___(__|___|_)\_)(__)(___|_)\_|__|___/ \__/   (_)(_|____)  (_/\/\_|___|_)\_)\__/   (___(___)
(  _|  \/  |  ,(  ) (  _)(  )(   \ /  \/ __)                                                
 ) _))    ( ) _/)(__ ) _)/__\ ) ) | () )__ \                                                
(___|_/\/\_|_) (____|___|_)(_|___/ \__/(___/                                                                                                                                                                                        
                                                                                                                              
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
                       """)
               
        opcion = (input("\nSelecione una de las opciones: "))
        
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                          RepEmpleado.menu()
                                   if (opcion == 2):
                                          CRUDempleado.menu()

                                   if (opcion == 0):
                                          break


#MENU GAMA

def menuGAMA():
       while True:
        os.system("clear")
        print("""
 ___ __ ___ _  _ _  _ ___ _  _ __ ___   __      __  __      __  __ ___ _  _ _  _    ___ ___ 
(  ,|  |  _| \( | )( |  _| \( |  |   \ /  \    (  )(  )    (  \/  |  _| \( | )( )  (   (  _)
 ) ,\)( ) _))  ( \\// ) _))  ( )( ) ) | () )   /__\ )(__    )    ( ) _))  ( )()(    ) ) ) _)
(___(__|___|_)\_)(__)(___|_)\_|__|___/ \__/   (_)(_|____)  (_/\/\_|___|_)\_)\__/   (___(___)
 / _)(  )(  \/  )(  )                                                                       
( (/\/__\ )    ( /__\                                                                       
 \__(_)(_|_/\/\_|_)(_)                                                                                                                                                     
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
                       """)
               
        opcion = (input("\nSelecione una de las opciones: "))
        
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                          Repgama.menu()
                                   if (opcion == 2):
                                          CRUDgama.menu()

                                   if (opcion == 0):
                                          break                     

#MENU OFICINA
                                   

def menuOFICINA():
       while True:
        os.system("clear")
        print("""
 ___ __ ___ _  _ _  _ ___ _  _ __ ___   __      __  __      __  __ ___ _  _ _  _    ___ ___ 
(  ,|  |  _| \( | )( |  _| \( |  |   \ /  \    (  )(  )    (  \/  |  _| \( | )( )  (   (  _)
 ) ,\)( ) _))  ( \\// ) _))  ( )( ) ) | () )   /__\ )(__    )    ( ) _))  ( )()(    ) ) ) _)
(___(__|___|_)\_)(__)(___|_)\_|__|___/ \__/   (_)(_|____)  (_/\/\_|___|_)\_)\__/   (___(___)
 /  (  _|  ) _|  | \( )(  )                                                                 
( () ) _))( (_ )( )  ( /__\                                                                 
 \__(_) (__)__|__|_)\_|_)(_)                                                                                                                                               
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
                       """)
               
        opcion = (input("\nSelecione una de las opciones: "))
        
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                          Repoficina.menu()
                                   if (opcion == 2):
                                          CRUDoficina.menu()

                                   if (opcion == 0):
                                          break     

                                                                                                                                                
#MENU PAGO

def menuPAGO():
       while True:
        os.system("clear")
        print("""
 ___ __ ___ _  _ _  _ ___ _  _ __ ___   __      __  __      __  __ ___ _  _ _  _    ___ ___ 
(  ,|  |  _| \( | )( |  _| \( |  |   \ /  \    (  )(  )    (  \/  |  _| \( | )( )  (   (  _)
 ) ,\)( ) _))  ( \\// ) _))  ( )( ) ) | () )   /__\ )(__    )    ( ) _))  ( )()(    ) ) ) _)
(___(__|___|_)\_)(__)(___|_)\_|__|___/ \__/   (_)(_|____)  (_/\/\_|___|_)\_)\__/   (___(___)
(  ,(  )/ _)/  \                                                                            
 ) _/__( (/( () )                                                                           
(_)(_)(_)__/\__/                                                                                                                                                                                                                   
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
                       """)
               
        opcion = (input("\nSelecione una de las opciones: "))
        
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                           Reppago.menu()
                                   if (opcion == 2):
                                          CRUDpago.menu()

                                   if (opcion == 0):
                                          break     
          
#MENU PEDIDO
                                   
def menuPEDIDIO():
       while True:
              os.system("clear")
              print("""
___ __ ___ _  _ _  _ ___ _  _ __ ___   __      __  __      __  __ ___ _  _ _  _    ___ ___ 
(  ,|  |  _| \( | )( |  _| \( |  |   \ /  \   (  )(  )    (  \/  |  _| \( | )( )  (   (  _)
 ) ,\)( ) _))  ( \\// ) _))  ( )( ) ) | () )   /__\ )(__    )    ( ) _))  ( )()(    ) ) ) _)
(___(__|___|_)\_)(__)(___|_)\_|__|___/ \__/   (_)(_|____)  (_/\/\_|___|_)\_)\__/   (___(___)
(  ,(  _|   (  |   \ /  \                                                                   
 ) _/) _)) ) )( ) ) | () )                                                                  
(_) (___|___(__|___/ \__/                                                                                                                                                                                                                                                                                      
             
                   1.Repotar los productos
                   2.Guardar actualizar y eliminar productos 
                   0.regresar al menu principal 
              
                       """)
                     
              opcion = input("\nSelecione una de las opciones: ")
              
              if re.match(r'[1-9]+$', opcion)is not None :
                     opcion =int(opcion)
                     
                     if (opcion == 1):
                            Reppedido.menu()
                     elif (opcion == 2):
                            CRUDpedido.menu()

                     elif (opcion == 0):
                            break     
                     


                                                     
