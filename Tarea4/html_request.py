import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs

def request_estructure():
    name_link = []
    link_request = []

    with open("Recursos/Urls.txt") as file:
        for link in file:
            if link != "- - - - - - - - - - Urls Disponibles - - - - - - - - - -" + "\n":
                for x in link:
                    if x == "/" or x == "\n" or x == ":" or x == "." or x == "?" or x == "*" or x == "|" or x == '"':
                        pass
                    else:
                        name_link.append(x)

                if not os.path.isfile("Recursos/" + str.join('', name_link) + ".txt"):
                    for y in link:
                        if y == "\n":
                            pass
                        else:
                            link_request.append(y)

                    not_request = re.compile(r'https://(www.)?(facebook)?(twitter)?(instagram)?(youtube)?(music.apple)?(open.spotify)?.com/')
                    if not_request.search(str.join('', link_request)):
                        pass
                    else:
                        page = requests.get(str.join('', link_request))
                        time.sleep(5)
                        if page.status_code == 200:
                            content = bs(page.content, "html.parser")
                            with open("Recursos/" + str.join('', name_link) + ".txt", "w", encoding='UTF-8') as file:
                                file.write(content.prettify())
                        else:
                            pass
                else:
                    pass
            else:
                pass
            name_link.clear()
            link_request.clear()