import socket
import time
import requests

class CloudMiddlebox:
    def __init__(self, client1_ip="192.168.10.15", client1_mac="32:04:0A:EF:19:CF", client2_ip="192.168.10.20", client2_mac="10:AF:CB:EF:19:CF", 
                 client3_ip="192.168.10.25", client3_mac="AF:04:67:EF:19:DA", router_mac="05:10:0A:CB:24:EF"):
        self.client1_ip_address = client1_ip 
        self.client1_mac_address = client1_mac 
        self.client2_ip_address = client2_ip  
        self.client2_mac_address = client2_mac  
        self.client3_ip_address = client3_ip  
        self.client3_mac_address = client3_mac  
        self.router_mac_address = router_mac
        
    def main(self):
        
        #URL of GCP instance endpoint  
        cloud_middlebox_url = 'https://us-central1-refined-analogy-334222.cloudfunctions.net/Encryption'

        #Create socket for router for receiving messages from server
        router_receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        router_receive_socket.bind(("localhost", 8100))

        #Create socket for router for sending messages to client
        router_send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        router_send_socket.bind(("localhost", 8200))

        server = ("localhost", 8000)

        router_send_socket.listen(4)
        client1 = None
        client2 = None
        client3 = None
        while (client1 == None or client2 == None or client3 == None):
            #Accepting connections from online clients
            client, address = router_send_socket.accept()
            
            if(client1 == None):
                client1 = client
                print("Client 1 is online")
            
            elif(client2 == None):
                client2 = client
                print("Client 2 is online")
            else:
                client3 = client
                print("Client 3 is online")
                
        arp_table_socket = {self.client1_ip_address : client1, self.client2_ip_address : client2, self.client3_ip_address : client3}
        arp_table_mac = {self.client1_ip_address : self.client1_mac_address, self.client2_ip_address : self.client2_mac_address, self.client3_ip_address : self.client3_mac_address}
        
        #Connect to the server
        router_receive_socket.connect(server) 
        
        while True:
            mystart = time.time()
            
            #Parse the received packet and extract the ip and mac addresses
            response = router_receive_socket.recv(1024)
            response =  response.decode("utf-8")
            
            source_mac = response[0:17]
            destination_mac = response[17:34]
            source_ip = response[34:45]
            destination_ip =  response[45:56]
            message = response[56:]
            
            #Redirecting the request to the cloud middlebox service
            myobj = {'data': str(destination_ip)}
            x = requests.post(cloud_middlebox_url, json = myobj)
            destination_ip = x.text
            
            print("The packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
            print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
            print("\nMessage: " + message)
            
            
            ethernet_header = self.router_mac_address + arp_table_mac[destination_ip]
            IP_header = source_ip + destination_ip
            packet = ethernet_header + IP_header + message
            
            destination_socket = arp_table_socket[destination_ip]
            myend = time.time()
            print("Total time taken for cloud instance to do processing: ", str(myend-mystart))
            destination_socket.send(bytes(packet, "utf-8"))
            time.sleep(2)
if __name__ == '__main__':
    CloudMiddlebox().main()