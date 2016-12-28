import mcrcon
import time
import random
import sys

#login.txt file should have address:port its first line
#and rcon password as its second line


try:
    with open("login.txt","r") as f:
        s = f.read()
        l = s.splitlines(False)
        ip_addr = l[0].split(":")[0]
        port = int(l[0].split(":")[1])
        passwd = l[1]

except FileNotFoundError:
    print("Login info not found, run setlogin.py first")
    sys.exit(1)
    
except IndexError:
    print("Malformed login info file, run setlogin.py please")
    sys.exit(1)
    

rcon = mcrcon.MCRcon()

print("Connecting to {}:{}".format(ip_addr,port))


rcon.connect(ip_addr,port)

while True:
    try:
        print("Logging in...")
        rcon.login(passwd)
        break
    except mcrcon.MCRconException as e:
        if e.args[0] == "Login failed":
            print("Login failed, run setlogin.py to update info")
            sys.exit(1)
        else: raise

rcon.command("say LET THE GAMES BEGIN")
print("LET THE GAMES BEGIN")

iters = random.randint(3,10)

for i in range(iters):
    t = random.randint(10,25)
    l = random.randint(5,15)
    time.sleep(t)
    rcon.command("say Levitation in {} seconds".format(l))
    print("Levitation in {} seconds".format(l))
    time.sleep(l)
    rcon.command("effect @a 25 1 127")
    print("Levitation applied")
    
rcon.disconnect()
