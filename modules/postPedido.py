import json
import requests
import os
import re
import modules.getPedido as Pe
from tabulate import tabulate

def guardarPedido():
    
    guardar=dict()
    while True:
        try:
            if not pedido.get("codigo_pedido"):
                codigo = input("ingrese el codigo del pedido: ")
                if re.match (r'^[0-9]+$',codigo) is not None:
                    codigo = int (codigo)
                    lalala = Pe.getAll