working_hours = float(input("Nhap so gio lam viec trong tuan: "))
hourly_rate = float(input("Nhap muc luong theo gio: "))

standard_hours = 44
if working_hours <= standard_hours:
    salary = working_hours * hourly_rate
else:
    overtime_hours = working_hours - standard_hours
    salary = standard_hours * hourly_rate + overtime_hours * hourly_rate * 1.5

print(f"So tien thuc nhan la: {salary}")
