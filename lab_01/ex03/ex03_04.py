items = tuple(input("Nhap cac phan tu tuple, cach nhau boi dau phay: ").split(","))
items = tuple(item.strip() for item in items)
if items:
    print(f"Phan tu dau tien: {items[0]}")
    print(f"Phan tu cuoi cung: {items[-1]}")
else:
    print("Tuple rong.")
