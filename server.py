import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

methods = "add, subtract, and quit" #possible operations

#Listens for connections and creates a connection with client (copied base-code section)
print("Listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()
    with conn:
        print(f"Connection established with {addr}")
        while True:
            data = conn.recv(1024) #recieved message: client's inputted name + also starts connection across server and client
            if not data:
                break

            print(f"Server received name: " + data.decode('utf-8')) #decoded message: client's inputted name
            print("Sending welcome to client...")
            conn.send(data) #sends decoded message back to client: client's inputted name

            print("Requesting possible methods...")
            print("Possible methods include: " + methods) #possible operations: "add, subtract, and quit"
            print("Echoing possible methods back to client...")
            conn.send(methods.encode('utf-8')) #sends list of methods/possible operations to client
            
            msg = conn.recv(1024).decode('utf-8') #decoded message: client's inputted method choice

            #Automatically quits the program if client doesn't choose any of the given methods/options
            if msg not in ['add', 'subtract', 'quit']:
                print("Client has chosen a non-acceptable method. Quitting program...")
                conn.send("Invalid method...".encode('utf-8')) #sends error message to client

            #Chooses the add method if client requests to add
            if msg == 'add':
                print("Client has requested to add")

                #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
                while True:
                    xNum = conn.recv(1024).decode('utf-8') # decoded message: client's inputted value for x. if this fails, repeat this until integer is sent
                    try:
                        int (xNum) #tries parsing Client's sent x value as an int
                        break #breaks out of while loop once integer has been entered
                    except ValueError: 
                        errorX = conn.recv(1024).decode('utf-8') #decoded message: "Error: Received an invalid input for x. Asking client to enter valid input..."
                        print(errorX) #prints error message
                print(f"Received x = {int(xNum)}") #Once integer has been entered, prints integer to server/server tracing, exits while loop

                #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
                while True:
                    yNum = conn.recv(1024).decode('utf-8') #decoded message: client's inputted value for y. if try statement fails, repeat this until integer is sent
                    try:
                        int (yNum) #tries parsing Client's sent y value as an int
                        break #breaks out of while loop once integer has been entered
                    except ValueError:
                        errorY = conn.recv(1024).decode('utf-8') #decoded message: "Error: Received an invalid input for y. Asking client to enter valid input..."
                        print(errorY) #prints error message
                print(f"Received y = {int(yNum)}") #Once integer has been entered, prints integer to server/server tracing, exits while loop

                print("Adding numbers...")
                intXNum = int (xNum) #parses clients inputted integer as an integer
                intYNum = int (yNum) #parses clients inputted integer as an integer
                sum = intXNum + intYNum 
                print(f"The sum of {intXNum} + {intYNum} is {sum}")
                print("Sending sum to client...")
                conn.sendall(str(sum).encode('utf-8')) #Sends sum value to client

            #Chooses the subtract method if client requests to subtract
            if msg == 'subtract':
                print("Client has requested to subtract")

                #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
                while True:
                    xNum = conn.recv(1024).decode('utf-8') #decoded message: client's inputted value for x. if try statement fails, repeat this until integer is sent
                    try:
                        int (xNum) #tries parsing Client's sent x value as an int
                        break #breaks out of while loop once integer has been entered
                    except ValueError:
                        errorX = conn.recv(1024).decode('utf-8') #decoded message: "Error: Received an invalid input for x. Asking client to enter valid input..."
                        print(errorX) #prints error message
                print(f"Received x = {int(xNum)}") #Once integer has been entered, prints integer to server/server tracing, exits while loop

                #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
                while True:
                    yNum = conn.recv(1024).decode('utf-8') #decoded message: client's inputted value for y. if try statement fails, repeat this until integer is sent
                    try:
                        int (yNum) #tries parsing Client's sent y value as an int
                        break #breaks out of while loop once integer has been entered
                    except ValueError:
                        errorY = conn.recv(1024).decode('utf-8') #decoded message: "Error: Received an invalid input for y. Asking client to enter valid input..."
                        print(errorY) #prints error message
                print(f"Received y = {int(yNum)}") #Once integer has been entered, prints integer to server/server tracing, exits while loop

                print("Subtracting numbers...")
                intXNum = int (xNum) #parses clients inputted integer as an integer
                intYNum = int (yNum) #parses clients inputted integer as an integer
                difference = intXNum - intYNum
                print(f"The difference of {intXNum} - {intYNum} is {difference}")
                print("Sending sum to client...")
                conn.sendall(str(difference).encode('utf-8')) #Sends difference value to client

            #Quits program if client requests to quit
            if msg == 'quit':
                print("Client has chosen to quit")

#Exits program when operation is completed
print("Server is done!")