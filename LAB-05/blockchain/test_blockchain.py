from blockchain import Blockchain

# Testing the blockchain
my_blockchain = Blockchain()

# Adding transactions dynamically
while True:
    sender = input("Nhập người gửi (hoặc nhấn Enter để dừng): ")
    if sender == "":
        break
    receiver = input("Nhập người nhận: ")
    amount = input("Nhập số tiền: ")

    try:
        amount = float(amount)  # Đảm bảo amount là số
        my_blockchain.add_transaction(sender, receiver, amount)
    except ValueError:
        print("Số tiền phải là số hợp lệ. Hãy thử lại.")

# Mining a new block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Displaying the blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("\n")

# Check if the blockchain is valid
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
