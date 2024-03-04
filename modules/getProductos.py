import storage.producto as pro

def getAllProveedor(codigo):
    Nombre_proveedor =[ ] 
    for val in pro.produto:
       if(val.get("proveedor")=="Murcia Seasons"):
           Nombre_proveedor.append(val)
    return Nombre_proveedor





