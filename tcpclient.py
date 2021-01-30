import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('[+] Connecting to %s Port %s' % server_address)

with sock as s:
    s.connect((server_address))
    s.sendall(b'bowser,Windows')
    datab = s.recv(1024)

print('Received', repr(datab))
