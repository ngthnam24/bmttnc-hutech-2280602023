items = input("Nhap cac phan tu, cach nhau boi dau phay: ").split(",")
items = [item.strip() for item in items]
result = tuple(items)
print(result)
