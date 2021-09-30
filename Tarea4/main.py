import os
from Srch_links import OpenChrome
from webscrap import WebScraping

def new_srch():
    with open("Recursos/Urls.txt", "w") as file:
        file.write("- - - - - - - - - - Urls Disponibles - - - - - - - - - -\n")

    if os.path.isdir("Recursos"):
        for file_name in os.walk("Recursos"):
            if file_name[2][0] == "Urls.txt":
                pass
            else:
                for file in file_name[2]:
                    if ".txt" in file and file != "Urls.txt":
                        os.remove("Recursos/" + file)

def menu(nombre):
    while True:
        os.system('cls')
        print("Busqueda automatizada\n")
        op = input("[1] Iniciar con la busqueda [2] Salir \nElija su opcion: ")

        if op == "1":
            print("Buscando links relacionados...")
            OpenChrome(nombre)
            print("Hecho!")
            WebScraping(nombre)
        elif op == "2":
            exit()
        else:
            input("Esta opcion es invalida, presione 'enter' para continuar...")


if __name__ == '__main__':
    new_srch()
    nombre = input("Ingrese el nombre de la persona famosa: ")
    menu(nombre)