#Lets make a port scanner...
import socket
ip=input("Enter the target IP:")

print("Here  is your scanning report:\n")
def scanner(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)

    result=sock.connect_ex((ip,port))

    if(result==0):
        print(f"+ Port {port} is open")
        with open("ports.txt","a") as f:
            f.write(f"The port {port} is open"+ "\n")
    else:
        print(f"- Port {port} is not available for this scan!")

    sock.close()

for i in range(1,150):
    scanner(i)

