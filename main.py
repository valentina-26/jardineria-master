from tabulate import tabulate

import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficina as oficna
import modules.getClients as cliente
import modules.getPedido as pedidos
#import modules.getPago as Pago

print (tabulate(pedidos.getAllPedidosEntregadosEnero(), tablefmt = "rounded grid"))


