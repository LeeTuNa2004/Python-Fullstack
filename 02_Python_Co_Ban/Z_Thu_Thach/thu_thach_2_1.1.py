# So quan ly diem mon hoc
# Toi uu bang cach tach cac chuc nang ra thanh ham (Def) rieng

danh_sach_hoc_sinh = {
    "An": 4.5,
    "Binh": 7.0,
    "Chi": 9.0
}

def tinh_diem_tb(bang_diem):
    if not bang_diem:
        return 0.0
    diem_tong = 0.0
    dem = 0
    for diem in bang_diem.values():
        diem_tong += diem
        dem += 1
    return diem_tong / dem

def xem_bang_diem(bang_diem):
    print("\n=== Bang diem hoc sinh ===")
    if not bang_diem:
        print("Danh sach hoc sinh dang trong!")
        return
    stt = 0
    for ten, diem in bang_diem.items():
        stt += 1
        print(f"- {stt}: {ten} - {diem:,.2f} diem")
    diem_trung_binh = tinh_diem_tb(bang_diem)
    print(f"Diem trung binh la: {diem_trung_binh:,.2f} diem")

def cap_nhat_diem(bang_diem):
    print("Lua chon chuc nang chinh: ")
    print("A. Them / Sua diem hoc sinh")
    print("B. Xoa diem hoc sinh")
    print("C. Thoat chuc nang va quay ve Menu chinh")
    choice = input("Nhap chuc nang muon thao tac: ").strip().upper()
    if choice == "A":
        ten_hoc_sinh = input("Nhap ten hoc sinh: ").strip().title()
        if not ten_hoc_sinh:
            print("Ten hoc sinh khong duoc de trong!")
            return
        if ten_hoc_sinh in bang_diem:
            print(f"Hoc sinh '{ten_hoc_sinh}' da co '{bang_diem[ten_hoc_sinh]:,.2f} diem.")
            print("Nhap diem moi de cap nhat: ")
        else:
            print(f"Them hoc sinh moi: '{ten_hoc_sinh}': ")
        try:
            diem_moi = float(input("Nhap diem cua hoc sinh (0-10): "))
            if 0 <= diem_moi <= 10:
                bang_diem[ten_hoc_sinh] = diem_moi
                print(f"Da luu diem {diem_moi:,.2f} cho '{ten_hoc_sinh}'!")
            else:
                print("Loi: Diem phai nam trong khoang tu 0 den 10.")
        except ValueError:
            print("Loi: Vui long nhap diem bang so hop le!")
    elif choice == "B":
        ten_xoa = input("Nhap ten hoc sinh muon xoa: ").strip().title()
        if not ten_xoa:
            print("Ten hoc sinh khong duoc de trong!")
        elif ten_xoa in bang_diem:
            del bang_diem[ten_xoa]
            print(f"Da xoa hoc sinh '{ten_xoa}' khoi danh sach!")
        else:
            print(f"Khong tim thay hoc sinh '{ten_xoa}' trong danh sach!")
    elif choice == "C":
        print("Thoat chuc nang va quay lai Menu chinh.")
    else:
        print("Loi: Lua chon khong hop le!")

def loc_hoc_sinh_dat(bang_diem, diem_chuan):
    # Loc ra danh sach cac tuple (ten, diem) dat chuan de tach biet logic loc va in
    ket_qua = []
    for ten, diem in bang_diem.items():
        if diem >= diem_chuan:
            ket_qua.append((ten, diem))
    return ket_qua

while True:
    print("\n=== So quan ly diem mon hoc ===")
    print("1. Xem ket qua & Tinh diem trung binh")
    print("2. Cap nhat diem hoc sinh (Them / Sua / Xoa)")
    print("3. Loc danh sach hoc sinh dat diem chuan")
    print("4. Thoat chuong trinh")
    print("=" * 50)

    lua_chon = input("Nhap lua chon: ").strip()

    if lua_chon == "1":
        xem_bang_diem(danh_sach_hoc_sinh)
    elif lua_chon == "2":
        cap_nhat_diem(danh_sach_hoc_sinh)
    elif lua_chon == "3":
        if not danh_sach_hoc_sinh:
            print("Danh sach hoc sinh dang trong!")
        else:
            try:
                diem_chuan = float(input("Nhap diem chuan can loc: "))
                if 0 < diem_chuan <= 10:
                    danh_sach_dat = loc_hoc_sinh_dat(danh_sach_hoc_sinh, diem_chuan)
                    print(f"\nDanh sach hoc sinh dat diem chuan >= {diem_chuan:,.2f}: ")
                    if not danh_sach_dat:
                        print("Khong co hoc sinh nao dat diem chuan nay!")
                    else:
                        # Danh STT 1, 2, 3... tren dung danh sach da loc dat chuan
                        for stt, (ten, diem) in enumerate(danh_sach_dat, start=1):
                            print(f"- {stt}: {ten} - {diem:,.2f} diem")
                else:
                    print("Loi: Diem phai nam trong khoang 0 den 10!")
            except ValueError:
                print("Loi: Vui long nhap diem bang so hop le!")
    elif lua_chon == "4":
        print("Cam on da su dung. Xin hen gap lai!")
        break
    else:
        print("Loi: Lua chon khong phu hop. Vui long nhap lai!")
