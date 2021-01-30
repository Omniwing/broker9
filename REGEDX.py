import re

line = "b'bowser,Windows'"


searchObj = re.search('([^,]*), line\)

if searchObj:
   print (searchObj.group())

else:
   print ("Nothing found!!")

#   {'win10.openstacklocal': {'ret': {
#       'cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run': {
#           'name': 'Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName',
#           'changes': {'pid': 2740, 'retcode': 0, 'stdout': '\r\nUserName   \r\n--------   \r\nWIN10\\Admin',
#                       'stderr': ''}, 'result': True,
#           'comment': 'Command "Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName" run',
#           '__sls__': 'whois', '__run_num__': 0, 'start_time': '23:01:31.023874', 'duration': 359.663,
#           '__id__': 'find_user_win'}}, 'out': 'highstate', 'retcode': 0, 'jid': '20210112230130254881'}}
#   username = (ret['win10.openstacklocal'][
#       'cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run'][
#       'changes']['stdout'])

#{'win10.openstacklocal': False}









#{'win10minion2': {'ret': {
#    'cmd_|-find_user_win_|-Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName_|-run': {'name': 'Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName', 'changes': {'pid': 5980, 'retcode': 0, 'stdout': '\r\nUserName\r\n--------', 'stderr': ''}, 'result': True, 'comment': 'Command "Get-WmiObject -ComputerName localhost -Class Win32_ComputerSystem | Select-Object UserName" run', '__sls__': 'whois', '__run_num__': 0, 'start_time': '22:45:41.834544', 'duration': 375.242, '__id__': 'find_user_win'}}, 'out': 'highstate', 'retcode': 0, 'jid': '20210120224539644183'}}





#   {'saltminionevan.novalocal': {'ret': {'module_|-find_user_linux_|-status.w_|-run': {'name': 'status.w', 'changes': {
#       'ret': [{'idle': '?xdm?', 'jcpu': '1:53', 'login': '16:59', 'pcpu': '0.12s', 'tty': ':0', 'user': 'root',
#                'what': '/usr/libexec/gnome-session-binary --session gnome-classic'},
#               {'idle': '21:31', 'jcpu': '1.67s', 'login': '16:59', 'pcpu': '0.01s', 'tty': 'pts/0', 'user': 'root',
#                'what': 'w -fh'}]}, 'comment': 'Module function status.w executed', 'result': True, '__sls__': 'whois',
#                                                                                       '__run_num__': 0,
#                                                                                       'start_time': '18:00:11.232517',
#                                                                                       'duration': 34.316,
#                                                                                       '__id__': 'find_user_linux'}},
#                                 'out': 'highstate', 'retcode': 0, 'jid': '20210112230010494118'}}
#   username = (ret['saltminionevan.novalocal']['module_|-find_user_linux_|-status.w_|-run']['changes']
# )

#{'saltminion2': {'ret': {'module_|-find_user_linux_|-status.w_|-run': {'name': 'status.w', 'changes': {
#    'ret': []}, 'comment': 'Module function status.w executed', 'result': True, '__sls__': 'whois', '__run_num__': 0, 'start_time': '17:42:58.695025', 'duration': 15.705, '__id__': 'find_user_linux'}},
#                                 'out': 'highstate', 'retcode': 0, 'jid': '20210119224259917681'}}