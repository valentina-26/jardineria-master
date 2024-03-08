import storage.pago as pag

     #listado con pagos 2008 mediante paypal(ordenar mayor a menor) EJERCICIO 13

def getAllPagosFecha():
    pagosFecha = []
    for val in pag.pago:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)

    return pagosFecha
  
  
  
    #TODAS LAS FORMAS DE PAGO EJERCICIO 14 
def getAllFormasPago():
    formadepago = []
    for val in pag.pago:
        val.get("forma_pago")
        formadepago.append(val.get("forma_pago"))
        convertir = set(str(item)for item in formadepago)
     
    return convertir 

   
    
    
    
    
    