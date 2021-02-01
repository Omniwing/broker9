import salt.client
import re
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
client = salt.client.LocalClient()

def findl(myuser):
    retl = client.cmd('os:Centos',
                     'state.sls',
                     ['whois'],
                     tgt_type = 'grain',
                     full_return=False)


    keylist = list(retl.keys())
    for x in keylist:
        if (retl[x] == False):  #if the machine is known but unresponsive it will return keyname False
            print(x, 'is nonresponsive')
            continue
        else:
            username = ((retl[x]['module_|-find_user_linux_|-status.w_|-run']['changes'])) #digging into nested dicts
            username2 = (username['ret'])
            if  username2 == []:
                user = 'null'
            else:
                username3 = (username2[0])
                user = (username3['user'])
            if user == myuser:
                comp4u = x
                return comp4u

            if user == 'null':
                comp4u = x

            else:
                comp4u = 'used'
    if comp4u == 'used':
        return 'all vms in use'
    else:
        return comp4u

def findw(myuserw):
    retw = client.cmd('os:Windows',
                     'state.sls',
                     ['whois'],
                     tgt_type = 'grain',
                     full_return=False)

    keylistw = list(retw.keys())
    for y in keylistw:
        if not retw[y]:
            print(y, 'is unresponsive')
            continue
        else:
            userw = retw[y]['cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run']['changes']['stdout']
            searchObj = re.search(('(?<=\\\)\w+'), userw)
            if searchObj:
                userw = searchObj.group()
            else:
                userw = 'null'
            if userw == myuserw:
                comp5u = y
                return comp5u

            if userw == 'null':
                comp5u = y
            else:
                comp5u = 'used'
    if comp5u == 'used':
        return 'all vms in use'
    else:
        return comp5u

with sock as s:
    s.bind(server_address)
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(512)
            datars = data.decode("utf-8")
            username2, sep, op = datars.partition(",")
            user2 = username2.strip("''")
            os = op.strip("'")
            if os == 'Centos':
                answer = findl(user2).encode()
            elif os == 'Windows':
                answer = findw(user2).encode()
            else:
                answer = ('Received data incorrectly formatted, terminating connection').encode()
            conn.sendall(answer)
            conn.close()



