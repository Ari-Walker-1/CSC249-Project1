import socket

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server

#Baseline code to get the client to actually run
def run_client():
    print("Client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"Connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(client):
                break

#Method that allows communication between client and server
def talk_to_server(client):

    #asks client for name and then stores it as a variable and sends the input to the server
    Input = input("Enter your name: ")
    client.sendall(Input.encode('utf-8')) #sends client's inputted name to server

    name = client.recv(1024).decode('utf-8') #decoded message: client's inputted name
    print(f"Welcome, " + name)

    print("Generating possible methods from server...")
    methods = client.recv(1024).decode('utf-8') #decoded message: "add, subtract, and quit"
    print(f"Possible methods: " + methods)

    #asks client what method they would like to ask the server for and stores it as a variable to send to server
    msg = input("What method would you like to ask the server to process? ")
    client.sendall(msg.encode('utf-8'))

    #Automatically quits the program if client doesn't choose any of the given options
    if msg not in ['add', 'subtract', 'quit']:
        invalid = client.recv(1024).decode('utf-8') #decoded message: "Invalid method..."
        print(invalid)

    #Chooses the add method if client requests to add
    if msg == 'add':

        #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
        while True:
            x = input("Please enter an integer value for x: ") #if try statement fails, repeat this until integer is sent
            try:
                int(x) #tries parsing Client's inputted x value as an int
                client.sendall(x.encode('utf-8')) #sends parsed x value to server
                break #breaks out of while loop once integer has been entered
            except ValueError: #runs if try block fails
                client.sendall(x.encode('utf-8')) #sends inputted x value to server
                print("Invalid input...")
                #sends error message to client
                client.sendall("Error: Received an invalid input for x. Asking client to enter valid input...".encode('utf-8'))

        #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
        while True:
            y = input("Please enter an integer value for y: ") #if try statement fails, repeat this until integer is sent
            try:
                int(y) #tries parsing Client's inputted y value as an int
                client.sendall(y.encode('utf-8')) #sends parsed y value to server
                break #breaks out of while loop once integer has been entered
            except ValueError: #runs if try block fails
                client.sendall(y.encode('utf-8')) #sends inputted y value to server
                print("Invalid input. Please enter an integer.")
                #sends error message to client
                client.sendall("Error: Received an invalid input for y. Asking client to enter valid input...".encode('utf-8'))

        print("Getting sum of x + y from server...")
        sum = client.recv(1024).decode('utf-8') #decoded message: calculated sum of x+y
        print("Your sum is: " + sum)
    

    #Chooses the subtract method if  client requests to subtract
    if msg == 'subtract':

        #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
        while True:
            x = input("Please enter an integer value for x: ") #if try statement fails, repeat this until integer is sent
            try:
                int(x) #tries parsing Client's inputted x value as an int
                client.sendall(x.encode('utf-8')) #sends parsed x value to server
                break #breaks out of while loop once integer has been entered
            except ValueError: #runs if try block fails
                client.sendall(x.encode('utf-8')) #sends inputted x value to server
                print("Invalid input...")
                #sends error message to client
                client.sendall("Error: Received an invalid input for x. Asking client to enter valid input...".encode('utf-8'))

        #Creates a loop that keeps going until client inputs an integer number (error handling for non integer entries)
        while True:
            y = input("Please enter an integer value for y: ") #if try statement fails, repeat this until integer is sent
            try:
                int(y) #tries parsing Client's inputted y value as an int
                client.sendall(y.encode('utf-8')) #sends parsed y value to server
                break #breaks out of while loop once integer has been entered
            except ValueError: #runs if try block fails
                client.sendall(y.encode('utf-8')) #sends inputted y value to server
                print("Invalid input. Please enter an integer.")
                #sends error message to client
                client.sendall("Error: Received an invalid input for y. Asking client to enter valid input...".encode('utf-8'))

        print("Getting difference of x - y from server...")
        difference = client.recv(1024).decode('utf-8') #decoded message: calculated difference of x-y
        print("Your difference is: " + difference)
        
    #Quits program if client requests to quit
    if msg == 'quit':

        print("Quitting...")
        return False #ends the socket connection by breaking out of talk_to_server method/ends run_client

#Main method 
if __name__ == "__main__":
    run_client() #Runs client
    print("Program completed! Exiting...") #Exits program