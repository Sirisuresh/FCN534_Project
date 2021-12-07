import socket

class Server:
    def __init__(self, server_ip="92.10.10.10", server_mac="00:00:0A:BB:28:FC", router_mac="05:10:0A:CB:24:EF"): 
        self.server_ip_address = server_ip
        self.server_mac_address = server_mac
        self.router_mac_address = router_mac
            
    def main(self):
        
        #Creating a socket for the enterprise server, binding to the port and listening for requests
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 8000))
        server_socket.listen(2)

        #Accepting a connection from the client
        '''
        while not router_connection == None:
            router_connection, address = server_socket.accept()
        '''

        while True:
            router_connection, address = server_socket.accept()
            if(router_connection != None):
                print(router_connection)
                break
        while True:
            ethernet_header = ""
            ip_header = ""
            
            #Inputting data and client IP from the terminal
            payload = input("\nData to send: ")
            destination_ip = input("Enter the IP of the client to send the message to:\n1. 92.10.10.15\n2. 92.10.10.20\n3. 92.10.10.25\n")
            
            if(destination_ip == "92.10.10.15" or destination_ip == "92.10.10.20" or destination_ip == "92.10.10.25"):
                
                #Creating packet as ethernet_header + ip_header + payload
                source_ip_address = self.server_ip_address
                #Creating IP Header as source_ip_address + destination_ip
                ip_header = ip_header + source_ip_address + destination_ip
                #Creating Ethernet Header as source_mac_address + destination_mac_address
                source_mac_address = self.server_mac_address
                destination_mac_address = self.router_mac_address 
                ethernet_header = ethernet_header + source_mac_address + destination_mac_address
                
                packet = ethernet_header + ip_header + payload
                
                router_connection.send(bytes(packet, "utf-8"))  
            else:
                print("Wrong client IP inputted")
if __name__ == '__main__':
    Server().main()