import re
import socket
import salt.client
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
client = salt.client.LocalClient()
logfile = "/root/PycharmProjects/pythonProject/venv/broker9/work2.log"

def findl(myuser):
    now = time.strftime("%b %d %Y %-I:%M %p")
    retl = client.cmd('os:Centos',
                     'state.sls',
                     ['whois'],
                     tgt_type = 'grain',
                     full_return=False)


    keylist = list(retl.keys())
    for x in keylist:
        if (retl[x] == False):  #if the machine is known but unresponsive it will return keyname False
            print(x, "is unresponsive")

            with open(logfile, 'a') as file:
                file.write(str(now) + ": " + str(x) + "is unresponsive!\n")
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
                with open(logfile, 'a') as file:
                     file.write(str(now) +": User \"" + str(myuser) + "\" is already logged into " + str(comp4u) + ", attempting to reconnect\n")
                return comp4u
                break

            if user == 'null':
                comp4u = x
                with open(logfile, 'a') as file:
                    file.write(str(now) + ": Found vacant VM \"" + str(comp4u) + "\", assigning to " + str(myuser) + "\n")
                return comp4u
            else:
                comp4u = 'used'
    if comp4u == 'used':
         with open(logfile, 'a') as file:
            file.write(str(now) +": All VMs in use\n")
#        basiclogging.info("No vacant VMs found")
         return 'all vms in use'
    else:
         print("found vacant vm", comp4u, "assigning to", myuser)
#         with open(logfile, 'a') as file:
#            file.write(str(now) + ": Found vacant VM \"" + str(comp4u) + "\", assigning to " + str(myuser) + "\n")
#        basiclogging.info("Found vacant VM %s for %s",  comp4u, myuser)
         return comp4u

def findw(myuserw):
    now = time.strftime("%b %d %Y %-I:%M %p")
    retw = client.cmd('os:Windows',
                     'state.sls',
                     ['whois'],
                     tgt_type = 'grain',
                     full_return=False)

    keylistw = list(retw.keys())
    for y in keylistw:
        if not retw[y]:
            with open(logfile, 'a') as file:
                file.write(str(now2) +": " + str(y) + " is unresponsive!\n")
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
                with open(logfile, 'a') as file:
                     file.write(str(now) +": User \"" + str(myuserw) + "\" is already logged into " + str(comp5u) + ", attempting to reconnect\n")
#                basiclogging.info("%s already logged into %s, attempting reconnect", myuserw, comp5u)
                return comp5u
                break
            if userw == 'null':
                comp5u = y
                with open(logfile, 'a') as file:
                    file.write(str(now) + ": Found vacant VM \"" + str(comp5u) + "\", assigning to " + str(myuserw) + "\n")
                return comp5u
                break
            else:
                comp5u = 'used'
    if comp5u == 'used':
        with open(logfile, 'a') as file:
            file.write(str(now) + ": All VMs in use\n")
        return 'all vms in use'
    else:
#        basiclogging.info("Found vacant VM %s for %s", y, myuserw)
        return comp5u

with sock as s:
    s.bind(server_address)
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
#            basiclogging.info("Connected by %s:%s", *addr)
            data = conn.recv(512)
            datars = data.decode("utf-8")
            username2, sep, op = datars.partition(",")
            user2 = username2.strip("''")
            os = op.strip("'")
#            basiclogging.info("User %s is requesting %s VM", user2, os)
            if os == 'Centos':
                answer = findl(user2).encode()
            elif os == 'Windows':
                answer = findw(user2).encode()
            else:
                answer = ('Received data incorrectly formatted, terminating connection').encode()
#                basiclogging.info("Received data was incorrectly formatted, connection terminated")
            conn.sendall(answer)
            conn.close()



