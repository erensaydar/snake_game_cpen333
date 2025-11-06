# Names: Cameron Taylor, Eren Saydar
# Student numbers: 78955465, 15764186

from socket import *

import random, time

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

count = 1
totalPings = 5

while count < totalPings+1:
    message = "PING " + str(count) + " - hello world"
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    
    startTime = time.time()
    
    try:
        returnMessage, serverAddress = clientSocket.recvfrom(2048)
    except timeout:
        print("Request timed out")
        count += 1
        continue

    stopTime = time.time()

    RTT = (stopTime - startTime) * 1000

    print(f"The Round Trip Time (RTT) is {RTT} milliseconds")
    print(returnMessage.decode())
    
    count += 1

clientSocket.close()