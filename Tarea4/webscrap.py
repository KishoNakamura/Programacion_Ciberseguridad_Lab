from openpyxl import Workbook
from openpyxl.styles import Font

from html_request import request_estructure
from get_info import social_info
from get_concert import concert_info

book = Workbook()
sheet = book.active

def Doc_Excel(sheet, book, nombre):
    sheet['A1'] = "Redes Sociales"
    sheet['A1'].font = Font(bold=True)

    sheet.merge_cells('F1:J1')
    sheet['F1'] = "Conciertos de " + nombre
    sheet['F1'].font = Font(bold=True)

    sheet['F2'] = "Nombre"
    sheet['F2'].font = Font(italic=True)
    sheet['G2'] = "Lugar"
    sheet['G2'].font = Font(italic=True)
    sheet['H2'] = "Fecha"
    sheet['H2'].font = Font(italic=True)
    sheet['I2'] = "Hora"
    sheet['I2'].font = Font(italic=True)
    sheet['J2'] = "Precio"
    sheet['J2'].font = Font(italic=True)

    sheet['L1'] = "Noticias"
    sheet['L1'].font = Font(bold=True)

    book.save(nombre + '.xlsx')

def WebScraping(nombre):
    print("\nCreando documento de excel...")
    Doc_Excel(sheet, book, nombre)
    print("Hecho!")

    print("\nObteniendo codigo fuente de las paginas...")
    request_estructure()
    print("Hecho!")

    print("\nObteniendo informacion personal y social...")
    social_info(sheet, book, nombre)
    print("Hecho!")

    print("\nObteniendo informacion de proximos conciertos...")
    concert_info(sheet, book, nombre)
    print("Hecho!")

    print("\n\nSe ha termiando el proceso de busqueda!, se ha creado un archvio de excel (" + nombre + ".xlsx)")
    input("presione 'enter' para continuar...")
