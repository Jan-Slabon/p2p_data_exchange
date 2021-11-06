from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        if datagram.decode('utf-8') == "ready":
            self.clients.add(addr)
            print(addr)
        elif datagram.decode('utf-8') == "sending":
            self.transport.write("\n".join([str(x) for x in self.clients]).encode('utf-8'), addr)


if __name__ == "__main__":
    port = 9999
    reactor.listenUDP(port, Server())
    reactor.run()