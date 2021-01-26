import salt.client
import re
#Execute commands through salt master
client = salt.client.LocalClient()
#Apply state whois to all Centos machines, returns hostname and logged in user
retl = client.cmd('os:Centos',
                 'state.sls',
                 ['whois'],
                 tgt_type = 'grain',
                 full_return=False)


keylist = list(retl.keys())
for x in keylist:
    if (retl[x] == False):
        print(x, 'is nonresponsive')
    else:
        username = ((retl[x]['module_|-find_user_linux_|-status.w_|-run']['changes']))
        username2 = (username['ret'])
        if  username2 == []:
            user = 'null'
        else:
            username3 = (username2[0])
            user = (username3['user'])
        print(x,user)