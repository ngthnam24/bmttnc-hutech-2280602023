# Tạo danh sách chứa các số thỏa mãn điều kiện
j = []
# Duyệt qua các số trong khoảng từ 2000 đến 3200
for i in range(2000, 3201):
    # Kiểm tra số chia hết cho 7 và không phải là bội số của 5
    if (i % 7 == 0) and (i % 5 != 0):
        # Thêm số thỏa mãn vào danh sách
        j.append(str(i))
# In ra các số thỏa mãn điều kiện, ngăn cách bởi dấu phẩy
print(','.join(j))
