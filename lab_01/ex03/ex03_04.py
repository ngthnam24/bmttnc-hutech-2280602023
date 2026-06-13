def truy_cap_phan_tu(tuple_data):
    first = tuple_data[0]
    last = tuple_data[-1]
    return first, last
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tuple(numbers)
# Sử dụng hàm và in kết quả
first, last = truy_cap_phan_tu(my_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
