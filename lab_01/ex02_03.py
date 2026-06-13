# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
# Kiểm tra số chẵn hay số lẻ
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn.")
