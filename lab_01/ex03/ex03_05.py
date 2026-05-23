items = input("Nhap cac phan tu list, cach nhau boi dau phay: ").split(",")
items = [item.strip() for item in items]
result = {}
for item in items:
    result[item] = result.get(item, 0) + 1
print(result)
