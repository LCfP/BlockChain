import hashlib as hasher
import datetime as date

class Block:
    # This init function defines what the blocks in the chain will look like
    def __init__(self, index, timestamp, data, previous_hash):
        # each block is stored with a timestamp and an index
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    # To help ensure integrity throughout the blockchain, each block will have a self-identifying hash.
    # Each block will have a cryptographic hash of its index, timestamp, data and the hash of the previous block.
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    # Function that creates the first block in the chain.
    # This block is of index 0, and it has an arbitrary data value and an arbitrary value in the “previous hash” parameter.
    def create_genesis_block():
        # Manually construct a block with
        # index zero and arbitrary previous hash
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    # This function will take the previous block in the chain as a parameter,
    # create the data for the block to be generated, and return the new block with its appropriate data.
    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
