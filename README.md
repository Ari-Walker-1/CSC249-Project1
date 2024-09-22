Note: Run client.py and server.py and look at terminals to view command line trace

1. Overview of Application:
    - My application is a basic addition and subtraction calculator. My application takes in keyboard input from the client. The application opens a connection to the server and client, asks client for name, returns hello + name, and then asks client if they would like to add, subtract, or quit by listing the following methods to the client. The client can then decide what they would like to do, and the program will respond accordingly with the correct operation and then the application will quit when finished.


2. Client->Server Message Format: (Client = sent, Server = recieved)

    1st 
    - Sent: Input = input("Enter your name: "), client.sendall(Input.encode('utf-8'))
        - asks client for name and then stores it as a variable and sends the input to the server

    - Recieved: data = conn.recv(1024), print(f"Server received name: "+ data.decode('utf-8'))
        - server then saves recieved name in a variable and then decodes the recieved name in a print statement
    

    2nd
    - Sent: msg = input("What method would you like to ask the server to process? "), client.sendall(msg.encode('utf-8'))
        - asks client what method they would like to ask the server for and stores it as a variable to send to server
    
    - Recieved: msg = conn.recv(1024).decode('utf-8')
        - server recieved and decodes this input and stores it as a variable


    (Repeat 3-6 for subtract)

    3rd
    - Sent: x = input("Please enter an integer value for x: "), client.sendall(x.encode('utf-8'))
        - stores client's inputted value of x as a variable and then sends it to server 

    - Recieved: xNum = conn.recv(1024).decode('utf-8')
        - stores recived info as a variable and decodes it
    

    4th 
    - Sent: client.sendall("Error: Received an invalid input for x. Asking client to enter valid input...".encode('utf-8'))
        - sends error message to server if the client inputted a non-integer value for x

    - Recieved: errorX = conn.recv(1024).decode('utf-8')
        - recieves and decodes error message and saves it as a variable
    

    5th
    - Sent: y = input("Please enter an integer value for y: "), client.sendall(y.encode('utf-8'))
        - stores client's inputted value of y as a variable and then sends it to server

    - Recieved: yNum = conn.recv(1024).decode('utf-8')
        - stores recived info as a variable and decodes it
    

    6th
    - Sent: client.sendall("Error: Received an invalid input for y. Asking client to enter valid input...".encode('utf-8'))
        - sends error message to server if the client inputted a non-integer value for y

    - Recieved: errorY = conn.recv(1024).decode('utf-8')
        - recieves and decodes error message and saves it as a variable
      

3. Server->Client Message Format (Server = sent, Client = recieved)

    1st
    - Sent: conn.send(data)
        - sends the name (previously sent by client and stored as variable data) back to to client

    - Recieved: name = client.recv(1024).decode('utf-8')
        - recieves resent name and decodes it and stores that as a variable


    2nd
    - Sent: conn.send(methods.encode('utf-8'))
        - sends list of methods/possible operations to client
    
    - Recieved: methods = client.recv(1024).decode('utf-8')
        - saves recieved methods as a variable and decodes it 
    

    3rd
    - Sent: conn.send("Invalid method...".encode('utf-8'))
        - sends error message to client if client requests a invalid option for the method/operation

    - Recieved: invalid = client.recv(1024).decode('utf-8')
        - recieves error message and saves it in a variable and decodes it


    4rd
    - Sent: conn.sendall(str(sum).encode('utf-8'))
        - sends the sum of x + y to the client

    - Recieved: sum = client.recv(1024).decode('utf-8')
        - recieves and decodes the sum and saves it in a variable
    

    5th
    - Sent: conn.sendall(str(difference).encode('utf-8'))
        - sends the difference of x - y to the client

    - Recieved: difference = client.recv(1024).decode('utf-8')
        - recieves and decodes the sum and saves it in a variable


4. Example Output (Client/Server Trace if client chooses addition of 5+5):

    Client Trace:
    - Client starting - connecting to server at IP 127.0.0.1 and port 65432
    - Connection established
    - Enter your name: (Client enters name: n)
    - Welcome, n
    - Generating possible methods from server...
    - Possible methods: add, subtract, and quit
    - What method would you like to ask the server to process? (Client types: add)
    - Please enter an integer value for x: (Client types integer: 5)
    - Please enter an integer value for y: (Client types integer: 5)
    - Getting sum of x + y from server...
    - Your sum is: 10
    - Program completed! Exiting...

    Server Trace:
    - Listening for connections at IP 127.0.0.1 and port 65432
    - Connection established with ('127.0.0.1', 51277)
    - Server received name: n
    - Sending welcome to client...
    - Requesting possible methods...
    - Possible methods include: add, subtract, and quit
    - Echoing possible methods back to client...
    - Client has requested to add
    - Received x = 5
    - Received y = 5
    - Adding numbers...
    - The sum of 5 + 5 is 10
    - Sending sum to client...
    - Server is done!

5. Acknowledgments:
    - I didn't really ask anyone for help a lot on this assignment because I found it pretty straighforward,
    but I will acknowledge Sophia Manodori and Zoe Fingleton since I asked both of them to exchange programs
    and review my code/bounced ideas off each other. I would also like to acknowledge google, since I did manage to figure out a lot about sending and recieving messages through encoding and decoding from my google searches.

