import hashlib
import datetime as date
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Block class to represent each block in the blockchain


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

# Function to create the genesis block (first block in the blockchain)


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Function to generate the next block based on the previous one


def next_block(previous_block):
    index = previous_block.index + 1
    timestamp = date.datetime.now()
    data = f"Block #{index} data"
    previous_hash = previous_block.hash
    return Block(index, timestamp, data, previous_hash)

# Blockchain class to manage the blockchain and its blocks


class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.current_block = self.chain[0]

    def add_block(self):
        block_to_add = next_block(self.current_block)
        self.chain.append(block_to_add)
        self.current_block = block_to_add

    def get_chain(self):
        # Returns blockchain as a JSON-compatible format
        return [block.__dict__ for block in self.chain]

    def save_chain(self, filename="blockchain.json"):
        # Save blockchain to a JSON file
        with open(filename, "w") as file:
            json.dump(self.get_chain(), file, default=str, indent=4)


# Create the blockchain instance
blockchain = Blockchain()

# Add some blocks to the blockchain
for _ in range(5):
    blockchain.add_block()

# Route to retrieve blockchain data as JSON


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify(blockchain.get_chain())

# Route to save the blockchain to a JSON file


@app.route('/save', methods=['GET'])
def save_blockchain():
    blockchain.save_chain()
    return "Blockchain saved to blockchain.json!"


if __name__ == '__main__':
    app.run(debug=True)
