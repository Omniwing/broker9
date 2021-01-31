import salt.client
import re

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
print(findl('jimmy'))



