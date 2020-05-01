from hashlib import sha512
import secrets
import string


class BaseBlockChain():
    """
    Handles the basic functionality of creating
    and handling addition of blocks to the chain.
    """
    block_chain = []
    string_encoding = 'utf-8'

    def __init__(self, genesis_hash=None, genesis_string=None, str_length=9):
        """
        Initialises a block chain assuming genesis
        hash as hash of previous block.\n
        Otherwise provide a genesis_string to generate
        genesis hash.\n
        If both are left blank then hash is created from
        a random string of length str_length.
        """
        genesis_string = genesis_string or ''.join(
            secrets.choice(string.printable)
            for i in range(str_length)
        )
        genesis_hash = genesis_hash or sha512(
            bytes(genesis_string, 'utf-8')
        ).hexdigest()
        self.block_chain.append(genesis_hash)

    def get_chain(self):
        """
        Get a tuple of block hashes excluding the
        genesis block.
        """
        return tuple(self.block_chain[1:])

    def get_genesis_block(self):
        """Get the genesis block signature"""
        return self.block_chain[0]

    def get_last_block(self):
        """Get the last block of the chain"""
        return self.block_chain[-1]

    def add_block(self, transaction):
        """
        Generate and add block where each block contains 
        one transaction of single string type
        """
        prev_block = self.get_last_block()
        new_block = sha512(bytes(prev_block, self.string_encoding))
        self.push_block_to_chain(new_block.hexdigest())

    def push_block_to_chain(self, block):
        """
        Push the generated block to the blockchain
        """
        self.block_chain.append(block)

    def __str__(self):
        """String representation of the block chain"""
        string_representation = 'The Block Chain is:'
        for block in self.block_chain[1:]:
            string_representation += '\n' + block
        return string_representation
