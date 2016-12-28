import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)


import mcrcon
rcon = mcrcon.MCRcon()

try:
    with open("login.txt","r") as f:
        s = f.read()
        l = s.splitlines(False)
        ip_addr = l[0].split(":")[0]
        port = int(l[0].split(":")[1])
        passwd = l[1]

except FileNotFoundError:
    sys.exit(1)
    
except IndexError:
    sys.exit(1)

try:
    rcon.connect(ip_addr,port)
    rcon.login(passwd)
except mcrcon.MCRconException:
    sys.exit(1)

rcon.command("save-on")
rcon.command("say BACKUP COMPLETE")

rcon.disconnect()
