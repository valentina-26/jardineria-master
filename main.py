from tabulate import tabulate

import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficina as oficna
import modules.getClients as cliente
import modules.getPedido as pedidos

print (tabulate(pedidos.getAllPedidosEnero(), tablefmt = "rounded grid"))


