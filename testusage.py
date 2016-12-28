import os
import sys
import time
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

timelength = 3*3600 #3 hours
timeinterval = 60 #1 minute

n = timelength//timeinterval #number of intervals (not perfect, but overlaps are ok)

#if server is used while script is active, outputs 1 to server-used.txt

import mcrcon
rcon = mcrcon.MCRcon()

try:
    with open("login.txt","r") as f:
        s = f.read()
        l = s.splitlines(False)
        ip_addr = l[0].split(":")[0]
        port = int(l[0].split(":")[1])
        passwd = l[1]
    with open("server-used.txt","w") as f:
        print(0,file=f)


except FileNotFoundError:
    sys.exit(1)
    
except IndexError:
    sys.exit(1)


try:
    rcon.connect(ip_addr,port)
    rcon.login(passwd)
except mcrcon.MCRconException:
    sys.exit(1)

for i in range(n+1):
    if i: time.sleep(timeinterval)
    out = rcon.command("list")
    if out.split(':')[1]:
        with open("server-used.txt","w") as f:
            print(1,file=f)
        rcon.disconnect()
        sys.exit(0)

rcon.disconnect()
