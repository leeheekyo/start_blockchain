import kcoin.config as cfg
import kcoin.proof as proof
from kcoin.transaction import Transaction


class Miner:
    def __init__(self, account_id):
        self.account_id = account_id

    def __call__(self, blockchain):
        # Adding mining rewards
        transaction = Transaction(cfg.GENESIS_ACCOUNT_ID, self.account_id, cfg.AMOUNT_OF_REWARD)
        blockchain.add_transaction(transaction)

        # Make new block with transactions and hash of last block
        new_block = blockchain.new_block()

        # Proof of Work
        new_proof = proof.find_proof(new_block)

        new_block.proof = new_proof # block.header.hash()||new_proof == "0000..."

        blockchain.add_block(new_block)

        return new_block

