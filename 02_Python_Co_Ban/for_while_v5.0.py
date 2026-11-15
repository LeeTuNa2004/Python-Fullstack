# Vi dien tu thong minh - Menu tuong tac

so_du = 1000000.0

while True:
    print(f"===== He thong vi dien tu =====")
    print(f"1. Xem so du hien tai")
    print(f"2. Nap tien vao vi")
    print(f"3. Rut tien tu vi")
    print(f"4. Thoat chuong trinh")
    print(f"=" * 35)
    try:
        lua_chon = int(input("Nhap lua chon (1-4): "))
    except ValueError:
        print("Vui long chi nhap lua chon tu 1 den 4: ")
        continue

    if lua_chon == 1:
        print(f"- So du hien tai trong vi: {so_du:,.0f} VND \n")
    elif lua_chon == 2:
        so_du += 500000
        print(f"- Nap tien thanh cong. So du hien tai la: {so_du:,.0f} VND \n")
    elif lua_chon == 3:
        try:
            i = float(input("Nhap so tien muon rut: "))
        except ValueError:
            print("So tien khong hop le!")
            continue
        if i > so_du:
            print(f"Giao dich that bai: So du trong vi khong du.")
        else:
            so_du = so_du - i
            print(f"- So tien rut thanh cong: {i:,.0f} VND")
            print(f"- So du con lai trong tai khoan: {so_du:,.0f} VND \n")
    elif lua_chon == 4:
        print(f"Cam on da su dung dich vu vi dien tu. Hen gap lai! \n")
        break
    else:
        print(" Lua chon khong hop le. Vui long chon tu 1 den 4! \n")
