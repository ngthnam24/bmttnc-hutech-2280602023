import hashlib


def md5_hash(data: str) -> str:
    """Compute MD5 hash of input string."""
    return hashlib.md5(data.encode()).hexdigest()


if __name__ == "__main__":
    test_data = "Hello, World!"
    print(f"Input: {test_data}")
    print(f"MD5: {md5_hash(test_data)}")

    # Test multiple inputs
    tests = ["Python", "Cryptography", "Hash Function", "MD5 Demo"]
    for t in tests:
        print(f"MD5('{t}') = {md5_hash(t)}")
