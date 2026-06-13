from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Thêm các giao dịch
my_blockchain.add_transaction("Alice", "Bob", 10)
my_blockchain.add_transaction("Bob", "Charlie", 5)
my_blockchain.add_transaction("Charlie", "Alice", 3)

# Đào khối mới
my_blockchain.mine_pending_transactions("Miner")

# In chuỗi blockchain
my_blockchain.print_chain()

# Kiểm tra tính hợp lệ
print(f"\nIs Blockchain Valid: {my_blockchain.is_chain_valid()}")
