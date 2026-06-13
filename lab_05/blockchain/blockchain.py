from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 2
        self.create_genesis_block()

    def create_genesis_block(self):
        """Tạo khối đầu tiên (Genesis Block)"""
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """Lấy khối cuối cùng trong chuỗi"""
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """Thêm giao dịch vào danh sách chờ"""
        self.pending_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        })

    def mine_pending_transactions(self, miner_address):
        """Đào khối mới từ các giao dịch đang chờ"""
        # Thưởng cho thợ đào
        self.add_transaction("Genesis", miner_address, 1)

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        # Xóa danh sách giao dịch đang chờ
        self.pending_transactions = []

    def is_chain_valid(self):
        """Kiểm tra tính hợp lệ của chuỗi blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Kiểm tra hash của khối hiện tại
            if current_block.hash != current_block.calculate_hash():
                return False

            # Kiểm tra liên kết với khối trước
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        """In toàn bộ chuỗi blockchain"""
        for block in self.chain:
            print(block)
