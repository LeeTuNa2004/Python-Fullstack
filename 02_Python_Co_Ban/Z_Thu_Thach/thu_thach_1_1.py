# He thong quan ly chi tieu ca nhan - CLI
# dung vong lap

tong_thu = 0.0
tong_chi = 0.0

# Buoc 1: Tao khung Menu va dieu huong chuong trinh
while True:
    print("\n=== Ung dung quan ly chi tieu ca nhan - CLI ===")
    print("1. Them mot khoan giao dich moi (Thu nhap / Chi tieu): ")
    print("2. Xem tong hop so du hien tai (Tong thu / Tong chi / So du vi): ")
    print("3. Thoat chuong trinh")
    try:
        lua_chon = int(input("Nhap lua chon (1-3): "))
    except ValueError:
        print("Vui long chi nhap tu 1 den 3! \n")
        continue

    if lua_chon == 1:                                       # Buoc 2: Xu ly giao dich va cong don tai chinh
        print("\n--- Nhap giao dich moi ---")                    
        try:
            so_tien = float(input("Nhap so tien giao dich: "))
            loai = int(input("Phan loai giao dich (1: Thu nhap / 2: Chi tieu): "))
            if loai == 1:
                tong_thu += so_tien
                print(f"Da them thanh cong khoan thu: {so_tien:,.2f} VND")
            elif loai == 2:
                tong_chi += so_tien
                print(f"Da them thanh cong khoan chi: {so_tien:,.2f} VND")
            else:
                print("Loai giao dich khong hop le. Vui long chon 1 hoac 2!")
        except ValueError:
            print("Loi: Vui long chi nhap so hop le cho tien giao dich!")

    elif lua_chon == 2:                                     # Buoc 3: Hien thi bang tong hop va hoan thien CLI
        so_du = tong_thu - tong_chi
        print("\n" + "=" * 40)
        print("Bang tong hop tai chinh")
        print(f"- Tong thu nhap: {tong_thu:,.2f} VND")
        print(f"- Tong chi tieu: {tong_chi:,.2f} VND")
        print(f"- So du vi hien tai: {so_du:,.2f} VND")
        print("=" * 40)

    elif lua_chon == 3:
        print("Cam on da su dung. Xin chao va hen gap lai! \n")
        break

    else:
        print("Lua chon khong hop le. Vui long cho so tu 1 den 3!")
