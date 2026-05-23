x = int(input("Nhap X: "))
y = int(input("Nhap Y: "))

matrix = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i * j)
    matrix.append(row)

print(matrix)
