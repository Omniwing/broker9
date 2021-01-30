server1 = False
server2 = 'null'
server3 = 'jimmy'
serverlist = {server1, server2, server3}
def queryusername(x):

    for server in serverlist:
        if server == False:
            print(server, 'is unresponsive')
        if server == x:
            return ('connect to', s)
        else:
            return ('Connect to', x)

print(queryusername('blarg'))


# def findhost(myuser):
#     hostlist == {server1, server2, server}
#
#     for each host in hostlist:
#         user == queryusername(host)
#     if user == myuser:
#         return host
#     elif user == 'null'
#         return host
#     else
#         return 'no hosts available'
#
