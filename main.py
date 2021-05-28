import json
from spirecomm.communication.coordinator import Coordinator
from spiremine.Crypto.blocks import Block
from spiremine.Crypto.blocks import Blockchain

if __name__ == '__main__':
    coordinator = Coordinator()
    coordinator.signal_ready()
    with open('text.txt', 'w') as f:
        f.write('readme')
        f.close()
        