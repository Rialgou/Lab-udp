#!/usr/bin/env python3
import pathlib
from rudp import RUDPServer


def main():
    server = RUDPServer(10000)
    
    print("seleccione el directorio del que se descargaran los archivos: ")
    selection = input()
    dir_server = pathlib.Path(selection)
    
    contents = [content.name for content in dir_server.iterdir() if content.is_file()]
    print(contents)


    while True:
        message, address = server.receive()

        print(f"{address}: {message}")
        if(message == "DOWNLOAD"):
            #se devuelven los nombres de los archivos de la carpeta del serivdor
            server.reply(address,contents)
            #se recibe el nombre del archivo que quiere descargar el cliente
            message, address = server.receive()
            print(message)
            server.reply(address,"comenzando descarga de "+ message)
            #se abre el archivo y se guarda en una variable para posteriormente ser usado
            f = open("../server_files/h2.png","rb")
            file = f.read()
            f.close()
            server.reply(address, file)
            server.reply(address, "archivo enviado con exito")
            



        if (message == "exit"):
            server.reply(address,"Me muero")
            break
        



if __name__ == "__main__":
    main()
