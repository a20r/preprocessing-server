
import preprocessing
import sys
import socket

if __name__ == "__main__":
    if len(sys.argv) == 3:
        preprocessing.run(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        ip_addr = socket.gethostbyname(socket.getfqdn())
        preprocessing.run(ip_addr, 8000, sys.argv[1])
    else:
        raise Exception("Correct argument form not supplied")
