# The socket module
# To create a socket, we must use the socket.socket() function available
# in socket module, which has the general syntax:
#       s = socket.socket (socket_family, socket_type, protocol=0)
#
# Here is the description of the parameters:
#    socket_family: This is either AF_UNIX or AF_INET, as explained earlier.
#    socket_type: This is either SOCK_STREAM or SOCK_DGRAM.
#    protocol: This is usually left out, defaulting to 0.
#
# Server Socket Methods
#   s.bind()    |   binds address (host name, port number pair) to socket
#   s.listen()  |   sets up and start TCP listener
#   s.accept()  |   passively accepts TCP client connection, waiting until
#               |   connection arrives (blocking)
#
# Client Socket Methods
#   s.connect() |   actively initiates TCP server connection
#
# General Socket Methods
#   s.recv()    |   receives TCP message
#   s.send()    |   transmits TCP message
#   s.recvfrom()|   receives UDP message
#   s.sendto()  |   transmits UDP message
#   s.close()   |   closes socket
#   socket,gethostname()    | returns the hostname

"SERVER file"

# Echo server program
import socket                   # REQUIRED!

HOST = socket.gethostname()     # Symbolic name meaning all available interfaces
PORT = 50607                    # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    data = ''
    repstr = ''
    while data != b'12321':
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print('[Client says]', data)
            if not (data == b'12321'):
                repstr = b'Fail'
            else:
                repstr = b'Successful'
            print('-> ', repstr)
            conn.sendall(repstr)

# ====================================================
#       Read more about Socket Programming
# ====================================================
# 1. https://docs.python.org/3/library/socket.html
# 2. https://www.tutorialspoint.com/unix_sockets/index.htm
# 3. https://habrahabr.ru/post/149077/
