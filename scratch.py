import salt.client
import re
import socket


from datetime import datetime
ct = datetime.now(tz=None)
print(ct)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
client = salt.client.LocalClient()

with open("/root/PycharmProjects/pythonProject/venv/broker9/barbaroy.log", 'a') as logfile:
    logfile.write(ct.strftime("%b %d %Y %H:%M:%S"+"\n")
# def findl(myuser):
#     retl = client.cmd('os:Centos',
#                      'state.sls',
#                      ['whois'],
#                      tgt_type = 'grain',
#                      full_return=False)
#
#
#     keylist = list(retl.keys())
#     for x in keylist:
#         if (retl[x] == False):  #if the machine is known but unresponsive it will return keyname False
#             logging.info("%s is unresponsive", x)
#             continue
#         else:
#             username = ((retl[x]['module_|-find_user_linux_|-status.w_|-run']['changes'])) #digging into nested dicts
#             username2 = (username['ret'])
#             if  username2 == []:
#                 user = 'null'
#             else:
#                 username3 = (username2[0])
#                 user = (username3['user'])
#             if user == myuser:
#                 comp4u = x
#                 logging.info("%s already logged into %s, attempting reconnect",  myuser, comp4u)
#                 return comp4u
#                 break
#
#             if user == 'null':
#                 comp4u = x
#                 return comp4u
#                 break
#
#             else:
#                 comp4u = 'used'
#     if comp4u == 'used':
#         logging.info("No vacant VMs found")
#         return 'all vms in use'
#     else:
#         logging.info("Found vacant VM %s for %s",  comp4u, myuser)
#         return comp4u
#
# def findw(myuserw):
#     retw = client.cmd('os:Windows',
#                      'state.sls',
#                      ['whois'],
#                      tgt_type = 'grain',
#                      full_return=False)
#
#     keylistw = list(retw.keys())
#     for y in keylistw:
#         if not retw[y]:
#             logging.info("%s is unresponsive", y)
#             continue
#         else:
#             userw = retw[y]['cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run']['changes']['stdout']
#             searchObj = re.search(('(?<=\\\)\w+'), userw)
#             if searchObj:
#                 userw = searchObj.group()
#                 logging.info("BOBBY! BOBBY ARE YA %s THERE!" % (userw))
#             else:
#                 userw = 'null'
#             if userw == myuserw:
#                 comp5u = y
#                 logging.info("%s already logged into %s, attempting reconnect", myuserw, comp5u)
#                 return comp5u
#                 break
#             if userw == 'null':
#                 comp5u = y
#                 logging.info("assigning %s figured" % (y))
#                 return comp5u
#                 break
#             else:
#                 comp5u = 'used'
#     if comp5u == 'used':
#         logging.info("No vacant VMs found")
#         return 'all vms in use'
#     else:
#         logging.info("Found vacant VM %s for %s", y, myuserw)
#         return comp5u
#
# with sock as s:
#     s.bind(server_address)
#     s.listen()
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             logging.info("Connected by %s:%s", *addr)
#             data = conn.recv(512)
#             datars = data.decode("utf-8")
#             username2, sep, op = datars.partition(",")
#             user2 = username2.strip("''")
#             os = op.strip("'")
#             logging.info("User %s is requesting %s VM", user2, os)
#             if os == 'Centos':
#                 answer = findl(user2).encode()
#             elif os == 'Windows':
#                 answer = findw(user2).encode()
#             else:
#                 answer = ('Received data incorrectly formatted, terminating connection').encode()
#                 logging.info("Received data was incorrectly formatted, connection terminated")
#             conn.sendall(answer)
#             conn.close()
#             break



