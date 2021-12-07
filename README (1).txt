Please follow the following instructions to run our project code:

Step 1: Open 5 command prompt terminals in the folder containing the python files.

Step 2: Run server.py file using the command "python server.py" in first command prompt terminal.

Step 3: Run middlebox.py (or middlebox_Cloud.py to test cloud instance) file using the command "python middlebox.py" in next command prompt terminal.

Step 4: In the remaining three terminals, run the commands "python client1.py", "python client2.py", "python client3.py" in each terminal respectively. This will start our server side data input.

Step 5: On the server.py terminal, give the appropriate input for a message and the destination IP mentioned in the command prompt of server. These IPs would be the public IPs of the clients and would be taken as input for server.

Step 6: Check the middlebox terminal and client terminal to confirm if the packet has reached the client. The middlebox terminal also shows the delay for NAT processing.

The IP addresses of all clients and server is given below for reference. Please not while giving input to server for destination IP, make sure to give public IPs only as private IPs are not visible to server.


Server IP Address: 92.10.10.10

Client 1 IP Address (Private): 192.168.10.15
Client 1 IP Address (Public): 92.10.10.15

Client 2 IP Address (Private): 192.168.10.20
Client 2 IP Address (Public): 92.10.10.20

Client 2 IP Address (Private): 192.168.10.25
Client 2 IP Address (Public): 92.10.10.25