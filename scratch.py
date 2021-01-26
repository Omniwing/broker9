import salt.client
import re
#Execute commands through salt master
client = salt.client.LocalClient()
retw = client.cmd('os:Windows',
                 'state.sls',
                 ['whois'],
                 tgt_type='grain',
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
            print(y, 'null')