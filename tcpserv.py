import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

with sock as s:
    s.bind(server_address)
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(512)
            conn.sendall(data)
