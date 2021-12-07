import socket
import time
class Client3:
    def __init__(self, client_ip="192.168.10.25", client_mac="AF:04:67:EF:19:DA"):
        self.client_ip_address=client_ip
        self.client_mac_address=client_mac
        
    def main(self):            
        router = ("localhost", 8200)
        #Create a client socket and connect to the router
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(1)
        client_socket.connect(router)
        
        while True:
            #Parse the received packet and extract ip and mac addresses
            response = client_socket.recv(1024)
            response = response.decode("utf-8")
            source_mac = response[0:17]
            destination_mac = response[17:34]
            source_ip = response[34:45]
            destination_ip =  response[45:58]
            message = response[58:]
            
            print("\nPacket integrity:\ndestination MAC address matches client 3 MAC address: {mac}".format(mac=(self.client_mac_address == destination_mac)))
            print("\ndestination IP address matches client 3 IP address: {mac}".format(mac=(self.client_ip_address == destination_ip)))
            print("\nThe packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac=source_mac, destination_mac=destination_mac))
            print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))
            print("\nMessage: " + message)
if __name__ == '__main__':
    Client3().main()