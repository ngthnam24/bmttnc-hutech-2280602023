lines = []
print("Nhap cac dong, nhap dong rong de ket thuc:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line.upper())

for line in lines:
    print(line)
