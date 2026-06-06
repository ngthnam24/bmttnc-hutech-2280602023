import hashlib


def sha256_hash(data: str) -> str:
    """Compute SHA-256 hash of input string."""
    return hashlib.sha256(data.encode()).hexdigest()


if __name__ == "__main__":
    test_data = "Hello, World!"
    print(f"Input: {test_data}")
    print(f"SHA-256: {sha256_hash(test_data)}")

    # Test multiple inputs
    tests = ["Python", "Cryptography", "Hash Function", "SHA-256 Demo"]
    for t in tests:
        print(f"SHA-256('{t}') = {sha256_hash(t)}")

    # Demonstrate avalanche effect
    s1 = "Hello"
    s2 = "hello"
    print(f"\nAvalanche effect demonstration:")
    print(f"SHA-256('{s1}') = {sha256_hash(s1)}")
    print(f"SHA-256('{s2}') = {sha256_hash(s2)}")
