def setlogin():
    with open("login.txt","w") as f:
        addr =      input("Address:  ")
        port =  int(input("Port:     "))
        passwd =    input("Password: ")
        addr_str = "{}:{}".format(addr,port)
        print(addr_str,file=f)
        print(passwd,file=f)
        return (addr,port,passwd)

if __name__ == '__main__':
    setlogin()
