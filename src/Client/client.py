from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    def __init__(self, addr, port):
        self.location = (addr, port)  # your address
        self.server = ('127.0.0.1', 9999)  # this is sample address for your server on localhost and port 9999
        self.address = None  # address of another person
        print("running on: ", self.location)

    def startProtocol(self):
        print("Starting...")
        self.transport.write("ready".encode('utf-8'), self.server)

    def datagramReceived(self, datagram, addr):
        if addr == self.server:
            print("choose client you want to talk to: ")
            print(datagram.decode('utf-8'))
            self.address = input("Write host: "), int(input("Write port: "))
            reactor.callInThread(self.send_message())
        else:
            print(addr,":",datagram.decode('utf-8'))

    def send_message(self):
        while True:
            self.transport.write(input(">>>").encode('utf-8'), self.address)





if __name__ == "__main__":
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('127.0.0.1', port))
    reactor.run()
