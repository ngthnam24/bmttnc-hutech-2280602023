from QuanLySinhVien import QuanLySinhVien


def print_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")


def main():
    quan_ly = QuanLySinhVien()
    while True:
        print_menu()
        choice = input("Nhap lua chon: ")

        if choice == "1":
            quan_ly.them_sinh_vien()
        elif choice == "2":
            quan_ly.cap_nhat_theo_id(int(input("Nhap ID sinh vien: ")))
        elif choice == "3":
            quan_ly.xoa_theo_id(int(input("Nhap ID sinh vien: ")))
        elif choice == "4":
            keyword = input("Nhap ten can tim: ")
            result = quan_ly.tim_kiem_theo_ten(keyword)
            for sinh_vien in result:
                print(sinh_vien)
        elif choice == "5":
            quan_ly.sap_xep_theo_diem_trung_binh()
        elif choice == "6":
            quan_ly.sap_xep_theo_chuyen_nganh()
        elif choice == "7":
            quan_ly.hien_thi_danh_sach()
        elif choice == "0":
            break
        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    main()
