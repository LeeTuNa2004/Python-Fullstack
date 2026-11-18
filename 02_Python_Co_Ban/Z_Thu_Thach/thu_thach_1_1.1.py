# He thong quan ly chi tieu ca nhan - CLI
# dung ham

def xu_ly_giao_dich(tong_thu, tong_chi):
    print("\n--- Nhap khoan giao dich moi ---")
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
            print("Phan loai khong hop le. Chi chon 1 hoac 2!")
    except ValueError:
        print("Loi: Vui long chi nhap so hop le!")
    return tong_thu, tong_chi

def xem_so_du(tong_thu, tong_chi):
    so_du = tong_thu - tong_chi
    print("\n" + "=" * 40)
    print("--- Bang tong hop tai chinh ---")
    print(f"- Tong thu nhap: {tong_thu:,.2f} VND")
    print(f"- Tong chi tieu: {tong_chi:,.2f} VND")
    print(f"- So du vi hien tai: {so_du:,.2f} VND")
    print("=" * 40)

def main():
    tong_thu = 0.0
    tong_chi = 0.0

    while True:
        print("\n Ung dung quan ly chi tieu ca nhan - CLI")
        print("1. Them mot khoan giao dich moi")
        print("2. Xem tong hop so du hien tai")
        print("3. Thoat chuong trinh")

        try:
            lua_chon = int(input("Nhap lua chon (1-3): "))
        except ValueError:
            print("Loi: Vui long nhap so tu 1 den 3!")
            continue

        if lua_chon == 1:
            tong_thu, tong_chi = xu_ly_giao_dich(tong_thu, tong_chi)
        elif lua_chon == 2:
            xem_so_du(tong_thu, tong_chi)
        elif lua_chon == 3:
            print("\nCam on da su dung. Xin chao va hen gap lai!")
            break
        else:
            print("Lua chon khong hop le. Vui long chon tu 1 den 3!")

if __name__ == "__main__":
    main()
