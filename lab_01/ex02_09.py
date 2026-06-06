def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


number = int(input("Nhap mot so nguyen: "))
if is_prime(number):
    print(f"{number} la so nguyen to.")
else:
    print(f"{number} khong phai la so nguyen to.")
