# Names: Cameron Taylor, Eren Saydar
# Student numbers: 78955465, 15764186

from socket import *

import random, time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

count = 1
totalPings = 5

while count < totalPings+1:
    message, clientAddress = serverSocket.recvfrom(2048)
    returnMessage = "PING " + str(count) + " - ditto"

    #simulate variability in RTT
    waitTime = random.randrange(5, 50)/1000 
    time.sleep(waitTime)

    #simulate packet loss
    ignoreVal = random.randrange(1,100,1)
    if 1 <= ignoreVal <= 10:
        count += 1
        continue
    
    serverSocket.sendto(returnMessage.encode(), clientAddress)

    count += 1