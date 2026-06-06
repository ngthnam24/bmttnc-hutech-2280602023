import hashlib


def blake2b_hash(data: str, digest_size: int = 32) -> str:
    """Compute BLAKE2b hash of input string."""
    return hashlib.blake2b(data.encode(), digest_size=digest_size).hexdigest()


if __name__ == "__main__":
    test_data = "Hello, World!"
    print(f"Input: {test_data}")
    print(f"BLAKE2b: {blake2b_hash(test_data)}")

    # Test multiple inputs
    tests = ["Python", "Cryptography", "Hash Function", "BLAKE2 Demo"]
    for t in tests:
        print(f"BLAKE2b('{t}') = {blake2b_hash(t)}")

    # Test different digest sizes
    for size in [16, 32, 48, 64]:
        print(f"BLAKE2b({size}b)('{test_data}') = {blake2b_hash(test_data, size)}")
