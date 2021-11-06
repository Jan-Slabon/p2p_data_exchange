import client as cl
from twisted.internet import reactor
from random import randint

if __name__ == "__main__":
    port2 = randint(1000, 5000)
    sender = cl.Sender('127.0.0.1', port2)
    reactor.listenUDP(port2, sender)
    reactor.run()