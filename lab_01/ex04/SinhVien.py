class SinhVien:
    auto_id = 1

    def __init__(self, ten: str, gioi_tinh: str, chuyen_nganh: str, diem_trung_binh: float):
        self.id = SinhVien.auto_id
        SinhVien.auto_id += 1
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_trung_binh = diem_trung_binh

    def hoc_luc(self) -> str:
        if self.diem_trung_binh >= 8:
            return "Gioi"
        if self.diem_trung_binh >= 6.5:
            return "Kha"
        if self.diem_trung_binh >= 5:
            return "Trung binh"
        return "Yeu"

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, Ten: {self.ten}, Gioi tinh: {self.gioi_tinh}, "
            f"Chuyen nganh: {self.chuyen_nganh}, Diem TB: {self.diem_trung_binh}, "
            f"Hoc luc: {self.hoc_luc()}"
        )
