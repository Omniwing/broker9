import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
user = ""
os = ""
with sock as s:
    s.bind(server_address)
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(512)
            datars = data.decode("utf-8")
            username, sep, op = datars.partition(",")
            user = username.strip("''")
            os = op.strip("'")
            userback = user.encode()
            osback = os.encode()
            conn.sendall(userback)
print(userback)
print(osback)







