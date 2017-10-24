from Block import *

"""
Simple blockchain example based on the following tutorial:
https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
"""

# Create the blockchain and add the genesis block
blockchain = [Block.create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = Block.next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Hash: {}\n".format(block_to_add.hash))