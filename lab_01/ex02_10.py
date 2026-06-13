def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))
