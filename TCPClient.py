from socket import *

serverName = "192.168.0.2"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def checkInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def checkFloat(num):
    try: 
        float(num)
        return True
    except ValueError:
        return False
    


while True:
    

    while True:
        functionInput = input("Choose your function (Add, Subtract, Random): ")
        if functionInput.lower() == "add" or functionInput.lower() == "subtract" or functionInput.lower() == "random":
            clientSocket.send(functionInput.encode())
            break
        else:
            print("Enter a valid function input")
            

    while True:
        num1 = input("Enter the first number: ")
        if checkInt(num1) or checkFloat(num1):
            clientSocket.send(num1.encode())
            break
        else:
            print("Please enter a number, int or float")
            
    while True:
        num2 = input("Now enter the second number: ")

        if checkInt(num2) or checkFloat(num2):
            clientSocket.send(num2.encode())
            break
        else:
            print("Please enter a number, int or float")
            
    
    result = clientSocket.recv(1024)
    print(result.decode())

   
    while True:
        redo = input("Would you like to try again? y/n: ")
        if redo.lower() == "n":
            print("Goodbye Then")
            exit()
        elif redo.lower() == "y":
            break
        else:
            print("Please enter y for yes or n for no")


            


        
            
            

    
        
    

