from socket import *
import threading
from threading import *
from random import randint 


def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.0.2', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

def handleClient(connectionSocket, adress):
    
    #sentence = connectionSocket.recv(1024).decode()

   
    while True:

        try: 
            clientFunction = connectionSocket.recv(1024).decode()
            clientNum1 = connectionSocket.recv(1024).decode()
            clientNum2 = connectionSocket.recv(1024).decode()

            if not clientNum1 or not clientNum2:
                break

            if isInt(clientNum1) == False:
                num1 = float(clientNum1)
            else:
                num1 = int(clientNum1)

            if isInt(clientNum2) == False:
                num2 = float(clientNum2)
            else:
                num2 = int(clientNum2)
               
            str(clientFunction)
            

            def calculateInputs(function, num1, num2):

                if function.lower() == "random":

                    if num1 < num2:
                        randResult = randint(num1, num2)
                        return f" A random number between {num1} and {num2} = {randResult} "
                    else:
                        randResult = randint(num2, num1)
                        return f"A random number between {num2} and {num1} = {randResult} "
                elif function.lower() == "subtract":
                    if num1 < num2:
                        subResult = num2 - num1
                        return f"{num2} - {num1} = {subResult}" 
                    else:
                        subResult = num1 - num2
                        return f"{num1} - {num2} = {subResult}"
                elif function.lower() == "add":
                    addResult = num1 + num2
                    return f"{num1} + {num2} = {addResult}"
                else:
                    return "invalid function input"


            result = calculateInputs(clientFunction, num1, num2)
            print("sending:", result, f" to {adress}")
            connectionSocket.send(result.encode())

            
            
        except ConnectionAbortedError:
                   
            break

        except ConnectionResetError:
            
            
            break

    connectionSocket.close()
    print(f"Connection with {adress} closed")




       
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket, addr)).start()
    print(f"Client Connected: {addr}")
   






