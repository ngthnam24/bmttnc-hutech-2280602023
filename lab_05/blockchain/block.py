import hashlib
import time
import json


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Tính hash của khối"""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Đào khối - Proof of Work"""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return (
            f"\n{'='*50}\n"
            f"Block #{self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Transactions: {self.transactions}\n"
            f"Proof: {self.nonce}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
            f"{'='*50}"
        )
