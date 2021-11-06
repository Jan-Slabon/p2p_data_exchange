import client as cl
from twisted.internet import reactor
from random import randint

if __name__ == "__main__":
    port1 = randint(1000, 5000)
    receiver = cl.Receiver('127.0.0.1', port1)
    reactor.listenUDP(port1, receiver)
    reactor.run()
