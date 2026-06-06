binary_values = input("Nhap cac so nhi phan 4 chu so, cach nhau boi dau phay: ").split(",")
result = []
for value in binary_values:
    clean_value = value.strip()
    if clean_value and int(clean_value, 2) % 5 == 0:
        result.append(clean_value)
print(",".join(result))
