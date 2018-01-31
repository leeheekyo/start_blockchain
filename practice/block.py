import json
import hashlib
from time import time

difficulty = 4
proof_val = "0"

class Block:
    def __init__(self, index=0, timestamp=time(), data='{}', previousHash='') :
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash=previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self) :
        hashValString = ''
        hashValString += str(self.index)
        hashValString += str(self.previousHash)
        hashValString += str(self.timestamp)
        hashValString += str(self.data)
        hashValString += str(self.nonce)
        hashValJson = hashValString.encode()
        hashVal = str(hashlib.sha256(hashValJson).hexdigest())
        return hashVal

    def mineBlock(self, difficulty) :
        rightVal = proof_val*difficulty
        while(self.hash[:difficulty] != rightVal) :
            self.nonce += 1
            self.hash = self.calculateHash()
        print("Block minded : " + self.hash)

class Blockchain:
    def __init__(self) :
        self.chain = [self.createGenesisBlock()]
        self.difficulty = difficulty

    def createGenesisBlock(self) :
        block = Block(0, "30/01/2018", "Genesis block", "0")
        return block

    def getLatesBlock(self) :
        return self.chain[len(self.chain)-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatesBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self) :
        i = 1
        while(i < len(self.chain)):
            currentBlock = self.chain[i]
            previousHash = self.chain[i-1]

            if(currentBlock.hash != currentBlock.calculateHash()) :
                return False
            if(currentBlock.previousHash != previousHash.hash) :
                return False
            i += 1

        return True

coin = Blockchain()
print("Mining block 1...")
coin.addBlock(Block(1,"21/02/2018", {"amount" : 4}))
print("Mining block 2...")
coin.addBlock(Block(2,"21/02/2018", {"amount" : 8}))
