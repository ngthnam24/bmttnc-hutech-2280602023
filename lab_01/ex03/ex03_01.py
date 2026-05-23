numbers = list(map(int, input("Nhap cac so nguyen, cach nhau boi dau cach: ").split()))
total = 0
for number in numbers:
    if number % 2 == 0:
        total += number
print(f"Tong cac so chan la: {total}")
