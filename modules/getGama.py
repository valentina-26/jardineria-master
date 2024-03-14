import requests

def getAllGama():
    peticion = requests.get("http://172.16.100.130:5003")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = list()
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
     