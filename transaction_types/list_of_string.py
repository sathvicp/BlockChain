from basic_utils.base_block_chain import BaseBlockChain
from hashlib import sha512


class StringTransactionChain(BaseBlockChain):
    """
    The transaction type for this class is a tuple
    of transaction strings.\n
    Each transaction is a string and a block consists
    of a tuple of transactions.
    """

    def add_block(self, transactions):
        """
        Generate and add a block for transaction type:
        list/tuple of string transactions.
        """
        transactions = tuple(transactions)
        prev_block = self.get_last_block()
        new_block = sha512(bytes(prev_block, self.string_encoding))
        for trans in transactions:
            new_block.update(bytes(trans, self.string_encoding))
        self.push_block_to_chain(new_block.hexdigest())
