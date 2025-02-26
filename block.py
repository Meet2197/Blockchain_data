import hashlib
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   self.data.encode('utf-8') +
                   self.previous_hash.encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(previous_block):
    index = previous_block.index + 1
    timestamp = date.datetime.now()
    data = "Block #" + str(index)
    previous_hash = previous_block.hash
    return Block(index, timestamp, data, previous_hash)


blockchain = [create_genesis_block()]

num_of_blocks_to_add = 10
previous_block = blockchain[0]

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
