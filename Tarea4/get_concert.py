from openpyxl import Workbook
from bs4 import BeautifulSoup as bs

def concert_info(sheet, book, nombre):
    for file_name in os.walk("Recursos"):
            for name in file_name[2]:
                if ".txt" in name and name != "Urls.txt":
                    with open("Recursos/" + name, "r", encoding='UTF-8') as page_html:
                        soup = bs(page_html, "html.parser")

                        #Nombre
                        name = []
                        for nm in soup.find_all('a', class_="event-title"):
                            event = []
                            for i in str(nm.get('title')):
                                if i == "\n":
                                    pass
                                else:
                                    event.append(i)
                            name.append(str.join('', event))

                        #Fechas
                        datetime = []
                        for dt in soup.find_all('time', class_="event-start-time"):
                            dates = []
                            for i in str(dt.text):
                                if i == "\n" or i.isspace():
                                    pass
                                else:
                                    dates.append(i)
                            datetime.append(str.join('', dates))

                        #Lugares
                        place = []
                        for lg in soup.find_all('a', class_="venue-name"):
                            lugar = []
                            for i in str(lg.text):
                                if i == "\n" or i.isspace():
                                    pass
                                else:
                                    lugar.append(i)
                            place.append(str.join('', lugar))

                        #Precios
                        price = []
                        for p in soup.find_all('p', class_="event-price" ):
                            precio = []
                            for i in str(p.text):
                                if i == "\n" or i.isspace() or i.isalpha():
                                    pass
                                else:
                                    precio.append(i)
                            price.append(str.join('', precio))

                        #Hora
                        hour = []
                        for hr in soup.find_all('time', class_="time"):
                            time = []
                            for i in str(hr.text):
                                if i == "\n" or i.isspace():
                                    pass
                                else:
                                    time.append(i)
                            hour.append(str.join('', time))

                        if not datetime and not place and not price:
                            pass
                        else:
                            u = 3
                            for m in name:
                                sheet[f'F{u}'] = str(m)
                                u += 1

                            i = 3
                            for x in place:
                                sheet[f'G{i}'] = str(x)
                                i += 1
                            
                            o = 3
                            for y in datetime:
                                sheet[f'H{o}'] = str(y)
                                o += 1

                            t = 3
                            for n in hour:
                                sheet[f'I{t}'] = str(n)
                                t += 1

                            p = 3
                            for z in price:
                                sheet[f'J{p}'] = str(z)
                                p += 1

                            book.save(nombre + '.xlsx')