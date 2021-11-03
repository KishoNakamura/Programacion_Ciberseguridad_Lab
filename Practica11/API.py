from pyhunter import PyHunter
from openpyxl import Workbook
from openpyxl.styles import Font
import getpass


def Busqueda(organizacion):
    resultado = hunter.domain_search(company=organizacion, limit=1, emails_type='personal')
    return resultado
    
print("= = = = = = Script para buscar información = = = = = =")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datosEncontrados = Busqueda(orga)

if datosEncontrados is None:
    print("\nNo se ha encontrado ningun dato relacionado al dominio ingresado")
    exit()
else:
    print(datosEncontrados)
