# So quan ly diem mon hoc

# Buoc 1: Tao khung du lieu, ham tinh diem trung binh va Menu
danh_sach_hoc_sinh = {
    "An": 4.5,
    "Binh": 7.0,
    "Chi": 9.0
}

def tinh_diem_tb(bang_diem):
    # Tranh loi chia cho 0 (ZeroDivisionError) neu bang diem dang rong
    if not bang_diem:
        return 0.0
    # Dung tham so bang_diem thay vi bien toan cuc de ham tai su dung linh hoat
    diem_tong = 0.0
    dem = 0
    for diem in bang_diem.values():
        diem_tong += diem
        dem += 1
    diem_tb = diem_tong / dem
    return diem_tb

while True:
    print("\n=== So quan ly diem mon hoc ===")
    print("1. Xem bang diem & Tinh diem trung binh")
    print("2. Cap nhat diem hoc sinh (Them / Sua / Xoa): ")
    print("3. Loc danh sach hoc sinh dat diem chuan: ")
    print("4. Thoat chuong trinh")
    print("=" * 50)

    lua_chon = input("Nhap lua chon: ").strip()

    # Buoc 2: Thuc hien logic chuc nang 1
    if lua_chon == "1":
        stt = 0
        print("\n=== Bang diem hoc sinh ===")
        if not danh_sach_hoc_sinh:
            print("Danh sach hoc sinh dang trong!")
        else:
            for ten, diem in danh_sach_hoc_sinh.items():
                stt += 1
                print(f"- {stt}: {ten} - {diem:,.2f} diem")
            diem_trung_binh = tinh_diem_tb(danh_sach_hoc_sinh)
            print(f"Diem trung binh la: {diem_trung_binh:,.2f} diem")

    # Buoc 2: Thuc hien logic chuc nang 2
    elif lua_chon == "2":
        print("Lua chon chuc nang chinh: ")
        print("A. Them / Sua diem hoc sinh")
        print("B. Xoa diem hoc sinh")
        print("C. Thoat chuc nang")
        # .upper() tu dong viet hoa de go 'a' hay 'A' deu nhan
        choice = input("Nhap chuc nang muon thao tac: ").strip().upper()
        if choice == "A":
            # .title() tu dong viet hoa chu cai dau va viet thuong cac chu cai sau de dong nhat voi Key trong Dictionary
            them_hoc_sinh = input("Nhap ten hoc sinh: ").strip().title()
            if not them_hoc_sinh:
                print("Ten hoc sinh khong duoc de trong!")
            else:
                if them_hoc_sinh in danh_sach_hoc_sinh:
                    print(f"Hoc sinh '{them_hoc_sinh}' da co {danh_sach_hoc_sinh[them_hoc_sinh]:,.2f} diem. Nhap diem moi de cap nhat: ")
                else:
                    print(f"Them hoc sinh moi: '{them_hoc_sinh}': ")
                # Nhap va kiem tra diem cho ca truong hop them moi lan cap nhat ca diem moi va diem cu
                try:
                    diem_moi = float(input("Nhap diem cua hoc sinh (0-10): "))
                    if 0 <= diem_moi <= 10:
                        danh_sach_hoc_sinh[them_hoc_sinh] = diem_moi
                        print(f"Da luu diem {diem_moi:,.2f} cho '{them_hoc_sinh}'!")
                    else:
                        print("Loi: Diem phai nam trong khoang tu 0 den 10.")
                except ValueError:
                    print("Loi: Vui long nhap diem bang so hop le!")
        elif choice == "B":
            ten_xoa = input("Nhap ten hoc sinh can xoa: ").strip().title()
            if not ten_xoa:
                print("Ten hoc sinh khong duoc de trong!")
            elif ten_xoa in danh_sach_hoc_sinh:
                del danh_sach_hoc_sinh[ten_xoa]
                print(f"Da xoa hoc sinh '{ten_xoa}' khoi danh sach!")
            else:
                print(f"Khong tim thay hoc sinh '{ten_xoa}' trong danh sach!")
        elif choice == "C":
            print("Thoat chuc nang va quay lai Menu chinh.")
        else:
            print("Loi: Lua chon khong hop le!")

    # Buoc 3: Thuc hien logic chuc nang 3
    elif lua_chon == "3":
        if not danh_sach_hoc_sinh:
            print("Danh sach hoc sinh dang trong!")
        else:
            try:
                diem_chuan = float(input("Nhap diem chuan can loc: "))
                if 0 < diem_chuan <= 10:
                    stt = 1
                    co_hoc_sinh_dat = False
                    print("Danh sach hoc sinh dat diem chuan la: ")
                    for ten, diem in danh_sach_hoc_sinh.items():
                        if diem_chuan <= diem:
                            print(f"- {stt}: {ten} - {diem:,.2f} diem")
                            stt += 1
                            co_hoc_sinh_dat = True
                    if not co_hoc_sinh_dat:
                        print("Khong co hoc sinh nao dat diem chuan nay!")
                else:
                    print("Loi: Diem phai nam trong khoang tu 0 den 10.")
            except ValueError:
                print("Loi: Vui long nhap diem bang so hop le!")

    # Thoat chuong trinh
    elif lua_chon == "4":
        print("Cam on da su dung. Xin hen gap lai!")
        break
    else:
        print("Loi: Lua chon khong phu hop. Vui long nhap lai!")
