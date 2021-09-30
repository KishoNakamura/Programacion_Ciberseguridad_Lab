import requests
import re
from openpyxl import Workbook

def social_info(sheet, book, nombre):
    redes = []
    with open("Recursos/Urls.txt", "r") as file:
        for line in file:
            social = re.compile(r'https://(www.)?(facebook)?(twitter)?(instagram)?(youtube)?(music.apple)?(open.spotify)?.com/')
            if social.search(line):
                redes.append(line)
            else:
                pass
            
    x = 2
    for y in redes:
        sheet[f'A{x}'] = str(y)
        x += 1
    book.save(nombre + '.xlsx')

    notice = []
    with open("Recursos/Noticias.txt", "r", encoding='UTF-8') as file2:
        for line2 in file2:
            notice.append(line2)
    
    u = 2
    for z in notice:
        sheet[f'L{u}'] = str(z)
        u += 1
    book.save(nombre + '.xlsx')