
from spirecomm.communication.coordinator import Coordinator
from spiremine.Crypto.blocks import Block
from spiremine.Crypto.blocks import Blockchain

if __name__ == '__main__':
    coordinator = Coordinator()
    coordinator.signal_ready()
    my_file = open('test.txt', 'w')
    my_file.write('Communication Secured')
    
