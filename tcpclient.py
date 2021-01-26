import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('[+] Connecting to %s Port %s' % server_address)
sock.connect(server_address)
try:

    # Send data
    message = 'This is the message.  It will be repeated.'.encode()
    print('[+] Sending "%s"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('[+] Received "%s"' % data)

finally:
    print('[-] closing socket')
    sock.close()