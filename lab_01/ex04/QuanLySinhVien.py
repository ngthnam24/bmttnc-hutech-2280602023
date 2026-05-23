from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them_sinh_vien(self):
        ten = input("Nhap ten: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        chuyen_nganh = input("Nhap chuyen nganh: ")
        diem_trung_binh = float(input("Nhap diem trung binh: "))
        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.danh_sach.append(sinh_vien)

    def tim_theo_id(self, student_id: int):
        for sinh_vien in self.danh_sach:
            if sinh_vien.id == student_id:
                return sinh_vien
        return None

    def cap_nhat_theo_id(self, student_id: int):
        sinh_vien = self.tim_theo_id(student_id)
        if sinh_vien is None:
            print("Khong tim thay sinh vien.")
            return
        sinh_vien.ten = input("Nhap ten moi: ")
        sinh_vien.gioi_tinh = input("Nhap gioi tinh moi: ")
        sinh_vien.chuyen_nganh = input("Nhap chuyen nganh moi: ")
        sinh_vien.diem_trung_binh = float(input("Nhap diem trung binh moi: "))

    def xoa_theo_id(self, student_id: int):
        sinh_vien = self.tim_theo_id(student_id)
        if sinh_vien is None:
            print("Khong tim thay sinh vien.")
            return
        self.danh_sach.remove(sinh_vien)

    def tim_kiem_theo_ten(self, keyword: str):
        result = []
        for sinh_vien in self.danh_sach:
            if keyword.lower() in sinh_vien.ten.lower():
                result.append(sinh_vien)
        return result

    def sap_xep_theo_diem_trung_binh(self):
        self.danh_sach.sort(key=lambda sinh_vien: sinh_vien.diem_trung_binh)

    def sap_xep_theo_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda sinh_vien: sinh_vien.chuyen_nganh.lower())

    def hien_thi_danh_sach(self):
        if not self.danh_sach:
            print("Danh sach rong.")
            return
        for sinh_vien in self.danh_sach:
            print(sinh_vien)
