data = {"name": "Nam", "age": 20, "major": "CNTT"}
key = input("Nhap key can xoa: ")
if key in data:
    del data[key]
print(data)
