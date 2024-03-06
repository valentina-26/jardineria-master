from tabulate import tabulate

import modules.getClients as cliente
import modules.getEmpleados as empleados
import modules.getOficina as oficna

print (tabulate(empleados.GetAllNombreApellidoEmailJefe(), tablefmt="grid"))

