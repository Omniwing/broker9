import salt.client
import re
client = salt.client.LocalClient()
# retl = client.cmd('os:Centos',
#                  'state.sls',
#                  ['whois'],
#                  tgt_type = 'grain',
#                  full_return=False)
#
#
# #Turns returned dict into list. Extracts hostname and username or assigns username 'null' if vacant
# keylist = list(retl.keys())
# for x in keylist:
#     if (retl[x] == False):  #if the machine is known but unresponsive it will return keyname False
#         print(x, 'is nonresponsive')
#     else:
#         username = ((retl[x]['module_|-find_user_linux_|-status.w_|-run']['changes'])) #digging into nested dicts
#         username2 = (username['ret'])
#         if  username2 == []:
#             user = 'null'
#         else:
#             username3 = (username2[0])
#             user = (username3['user'])
#         print(x,user)

def availablew(username):
    retw = client.cmd('os:Windows',
                     'state.sls',
                     ['whois'],
                     tgt_type = 'grain',
                     full_return=False)

    keylistw = list(retw.keys())
    for y in keylistw:
        if not retw[y]:
            print(y, 'is unresponsive')
        else:
            userw = retw[y]['cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run']['changes']['stdout']
            searchObj = re.search(('(?<=\\\)\w+'), userw)
            if searchObj:
                print(y, searchObj.group())
            else:
                userw = 'null'
                print(y, userw)

datar = b'bowser,Windows'

availablew("shboom")


