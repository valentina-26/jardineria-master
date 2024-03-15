import re
import modules.postProducto as CRUDproducto
import modules.getProductos as Repproducto
#menu productos

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
        if(re.match(r'[1-9]+$', opcion)is not None ):
                            opcion =int(opcion)
                            if(opcion>=0 and opcion<=5):
              

                                   if (opcion == 1):
                                          Repproducto.menu()
                                   if (opcion == 2):
                                          CRUDproducto.menu()

                                   if (opcion == 0):
                                          break
