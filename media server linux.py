import socket
import threading
import os

PLAYPAUSE = "0"
VOLUP = "1"
VOLDOWN = "2"

port = 1200

#declare new udp socket
try:
    udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    udpServerSocket.bind((socket.gethostname(), port))
    print(f"socket bound {port}")
except Exception as e:
    print(e)


def commandListener():
    #listener for new commands
    try:
        while True:
            print("listening")
            bytesRecieved = udpServerSocket.recv(1024)
            print("command recieved")
            commandID = bytesRecieved.decode("utf-8")
            
            print(f"received {commandID} request")
            
            commandDelegation(commandID, address)
    except Exception as e:
        print(e)


def commandDelegation(commandID, address):
    #delegate which command is wanted
    if commandID == PLAYPAUSE:
        PLAY_PAUSE_COMMAND = "echo play pause command"
        
        executeCommand(PLAY_PAUSE_COMMAND)
        writeToScreen(commandID, "PP", address)
        
    elif commandID == VOLUP:
        VOLUME_UP_COMMAND = "echo voulme up command"
        
        executeCommand(VOLUME_UP_COMMAND)
        writeToScreen(commandID, "UP", address)
    elif commandID == VOLDOWN:
        VOLUME_DOWN_COMMAND = "echo volume down command"
        
        executeCommand(VOLUME_DOWN_COMMAND)
        writeToScreen(commandID, "down", address)
        

def executeCommand(sysCommand):
    #os.system(sysCommand)
    print(sysCommand)


def writeToScreen(lastCommand, info, address):
    print(f"{lastCommand}")
    
    if info != "":
        print(f"Recieved {info} request from {address}")


#on new thread
commandListener()

print("end")
