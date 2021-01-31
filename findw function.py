import salt.client
import re
client = salt.client.LocalClient()


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
                print('we think user', userw, 'is logged into', y)
            else:
                userw = 'null'
                print('we think nobody is logged into', y)
            if userw == myuserw:
                comp5u = y
                return comp5u
                print('this shouldnothappen')

            if userw == 'null':
                comp5u = y
                print('since nobody is loged into', y, 'were setting comp5u equal to it')
            else:
                comp5u = 'used'
    if comp5u == 'used':
        return 'all vms in use'
    else:
        return comp5u



print(findw('bob'))


