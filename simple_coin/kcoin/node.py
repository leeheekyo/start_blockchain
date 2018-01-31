import requests
from uuid import uuid4

from kcoin.blockchain import BlockChain


class Node:
    def __init__(self, id=None):
        self.id = id if id else self._generate_id()
        self.neighbor = set()

    @staticmethod
    def _generate_id():
        return str(uuid4()).replace('-', '') # ceate id for mining rewards

    def add(self, address):
        self.neighbor.add(address)

    def __len__(self):
        return len(self.neighbor)

    @staticmethod
    def fetch_neighbor_chain(address):
        if(address.find("http://") == -1):
            address = "http://"+address
        res = requests.get('{0}/chain'.format(address))
        return res.json()

    def consensus_with_neighbor(self, blockchain):
        # blockchain : obj
        new_blockchain = None
        max_length = len(blockchain)

        for node in self.neighbor:
            data = self.fetch_neighbor_chain(node)

            if data['length'] > max_length:
                new_blockchain = BlockChain(chain=data['chain'])

                if not new_blockchain.valid():
                    new_blockchain = None
                else:
                    max_length = len(new_blockchain)

        return new_blockchain
