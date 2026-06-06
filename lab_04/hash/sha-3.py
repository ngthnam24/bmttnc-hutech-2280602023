import hashlib


def sha3_256_hash(data: str) -> str:
    """Compute SHA3-256 hash of input string."""
    return hashlib.sha3_256(data.encode()).hexdigest()


if __name__ == "__main__":
    test_data = "Hello, World!"
    print(f"Input: {test_data}")
    print(f"SHA3-256: {sha3_256_hash(test_data)}")

    # Test multiple inputs
    tests = ["Python", "Cryptography", "Hash Function", "SHA-3 Demo"]
    for t in tests:
        print(f"SHA3-256('{t}') = {sha3_256_hash(t)}")
