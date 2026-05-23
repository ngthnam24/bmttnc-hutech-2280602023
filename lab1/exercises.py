def format_student_info(student_id: str, full_name: str, age: int, major: str) -> dict:
    return {
        "MSSV": student_id,
        "Ho ten": full_name,
        "Tuoi": age,
        "Nganh": major,
    }


def list_even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def find_primes(limit: int) -> list[int]:
    if limit < 2:
        return []

    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


def count_text_stats(text: str) -> dict:
    words = text.split()
    vowels = "aeiouAEIOU"
    return {
        "So ky tu": len(text),
        "So tu": len(words),
        "So nguyen am": sum(1 for char in text if char in vowels),
        "In hoa": text.upper(),
    }


def analyze_password_strength(password: str) -> dict:
    checks = {
        "Do dai >= 8": len(password) >= 8,
        "Co chu hoa": any(char.isupper() for char in password),
        "Co chu thuong": any(char.islower() for char in password),
        "Co chu so": any(char.isdigit() for char in password),
        "Co ky tu dac biet": any(not char.isalnum() for char in password),
    }
    score = sum(checks.values())
    if score == 5:
        level = "Manh"
    elif score >= 3:
        level = "Trung binh"
    else:
        level = "Yeu"

    return {
        "Mat khau": password,
        "Muc do": level,
        "Tieu chi dat": score,
        **checks,
    }
