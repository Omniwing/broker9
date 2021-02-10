# import salt.client
logfile = "/root/PycharmProjects/pythonProject/venv/broker9/workthistime.log"
# from datetime import datetime
# now = datetime.now()
# now2 = now.strftime("%H:%M:%S")
import time
now = time.strftime("%b %d %Y %-I:%M %p")

with open(logfile, 'a') as file:
    file.write(str(now2) +": 1\n")

file.write(str(now2) + ": Found vacant VM \"" + str(comp4u) + "\", assigning to " + str(myuser) + "\n")