import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

#exits cleanly only if people have been/are on the server

import mcrcon
rcon = mcrcon.MCRcon()

try:
    with open("login.txt","r") as f:
        s = f.read()
        l = s.splitlines(False)
        ip_addr = l[0].split(":")[0]
        port = int(l[0].split(":")[1])
        passwd = l[1]
    with open("server-used.txt","r") as f:
        s = f.read()
        if s[0] == "1":
            used = True
        else:
            used = False
        

except FileNotFoundError:
    sys.exit(1)
    
except IndexError:
    sys.exit(1)
    
try:
    rcon.connect(ip_addr,port)
    rcon.login(passwd)
    out = rcon.command("list")
    rcon.disconnect()

except mcrcon.MCRconException:
    out = "There are 0/20 players online:"

if out.split(':')[1] or used:
    sys.exit(0)
else:
    sys.exit(1)

