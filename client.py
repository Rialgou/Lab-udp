#!/usr/bin/env python3
import sys
import os
import time

from rudp import RUDPClient


def main():
    client = RUDPClient("localhost", 10000)

    while True:
        try:
            reply = client.send_recv(input())

            print(reply)

            select_file = client.send_recv(input())

            print(select_file)

            file = client.send_recv("ok")
            print(file)
            f = open("kkcopia.txt","w")
            f.write(file)
            f.close()
        except:
            print("no response; giving up", file=sys.stderr)

            # Necesitamos usar os._exit en lugar de sys.exit,
            # pues el proceso de esperar una respuesta del servidor
            # utiliza hilos y la salida "forzosa" que nos ofrece
            # os._exit mata esos hilos a la vez que mata el proceso
            # principal
            os._exit(1)

        time.sleep(1)


if __name__ == "__main__":
    main()
