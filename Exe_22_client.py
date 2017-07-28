# Echo client program
import socket

HOST = socket.gethostname()     # The remote host
PORT = 50607                    # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    log = input("Input byte-data: ")
    s.sendall(str.encode(log))
    data = s.recv(1024)
print('[Server says]', repr(data))
