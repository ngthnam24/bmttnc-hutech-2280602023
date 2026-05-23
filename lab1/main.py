from exercises import (
    analyze_password_strength,
    count_text_stats,
    find_primes,
    format_student_info,
    gcd,
    lcm,
    list_even_numbers,
)


def print_section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def demo_basic_python() -> None:
    print_section("LAB 1 - PYTHON CO BAN")

    student = format_student_info(
        student_id="22110001",
        full_name="Nguyen Van A",
        age=20,
        major="Cong nghe thong tin",
    )
    print("Thong tin sinh vien:")
    for key, value in student.items():
        print(f"- {key}: {value}")

    numbers = list(range(1, 21))
    evens = list_even_numbers(numbers)
    print(f"\nDay so: {numbers}")
    print(f"So chan: {evens}")

    a, b = 18, 24
    print(f"\nUCLN({a}, {b}) = {gcd(a, b)}")
    print(f"BCNN({a}, {b}) = {lcm(a, b)}")

    primes = find_primes(50)
    print(f"\nSo nguyen to nho hon hoac bang 50: {primes}")

    sample_text = "Bao mat thong tin nang cao"
    stats = count_text_stats(sample_text)
    print("\nThong ke chuoi:")
    for key, value in stats.items():
        print(f"- {key}: {value}")

    password = "BMTTNC@2026"
    password_result = analyze_password_strength(password)
    print("\nDanh gia mat khau:")
    for key, value in password_result.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    demo_basic_python()
