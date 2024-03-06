from tabulate import tabulate

import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficina as oficna

print (tabulate(clientes.getAllClientPaisRegionCiudad(None), tablefmt="grid"))


