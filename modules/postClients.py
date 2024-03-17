import os
import json
from tabulate import tabulate 
import requests


def postClients():

    clientes = dict()

    while True:
        try:

