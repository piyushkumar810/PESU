'''                    
                   UDP SOCKET PROGRAMMING
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        │                                     │
   👨‍💻 SERVER PARTNER                    👨‍💻 CLIENT PARTNER
        │                                     │
        │                                     │
        ▼                                     ▼
Create File                           Create File
udp_server.py                         udp_client.py
        │                                     │
        ▼                                     ▼
Paste Server Code                     Paste Client Code
        │                                     │
        ▼                                     ▼
Find IP Address                       Put Server IP
(ipconfig)                            in client code
        │                                     │
        ▼                                     ▼
Run Server                             Run Client
python udp_server.py                  python udp_client.py
        │                                     │
        ▼                                     ▼
Server waits                           Enter message
for message                            hello
        │                                     │
        └──────────────► SEND ◄──────────────┘
                         │
                         ▼
                Server receives message
                         │
                         ▼
                Converts to UPPERCASE
                         │
                         ▼
        ┌────────────── REPLY ───────────────┐
        │                                    │
        ▼                                    ▼
Client receives reply              Server prints message
HELLO                              hello

'''


'''

🖥 SERVER SIDE STEPS
1. Open CMD
2. Go to folder
3. Create udp_server.py
4. Paste server code
5. Save file
6. Find IP using ipconfig
7. Run:
   python udp_server.py
8. Wait for client


💻 CLIENT SIDE STEPS
1. Open CMD
2. Go to folder
3. Create udp_client.py
4. Paste client code
5. Replace server IP
6. Run:
   python udp_client.py
7. Enter message
8. Receive reply



📡 SERVER CODE
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("UDP Server is ready to receive")

while True:

    message, clientAddress = serverSocket.recvfrom(2048)

    modifiedMessage = message.decode().upper()

    print("Client Message:", message.decode())

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)



    
📡 CLIENT CODE
from socket import *

# Put server IP here
serverName = "192.168.1.5"

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Enter lowercase sentence: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print("From Server:", modifiedMessage.decode())

clientSocket.close()




🔍 FIND SERVER IP

Run:

ipconfig

Look for:

IPv4 Address

Example:

192.168.1.5

Put this IP in client code.

▶ RUN COMMANDS
SERVER
python udp_server.py
CLIENT
python udp_client.py


✅ EXPECTED OUTPUT
CLIENT SIDE
Enter lowercase sentence: hello
From Server: HELLO
SERVER SIDE
UDP Server is ready to receive
Client Message: hello


⚠ IMPORTANT UDP FUNCTIONS
Function	          Purpose
-------------------------------------
socket()	        Create socket
bind()	                Attach port
sendto()	        Send data
recvfrom()	        Receive data
close()	                Close socket


⚠ IMPORTANT MCQ POINTS
Concept	Answer
UDP Socket Type	SOCK_DGRAM
TCP Socket Type	SOCK_STREAM
UDP Nature	Connectionless
UDP Functions	sendto(), recvfrom()
TCP Functions	send(), recv()

'''