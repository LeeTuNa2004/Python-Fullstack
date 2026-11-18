# Tro choi Oan Tu Ti (Rock-Paper-Scissors)

import random

thang = 0
thua = 0
hoa = 0

while True:
    print("Tro choi Rock-Paper-Scissors")
    print("1. Keo")
    print("2. Bua")
    print("3. Bao")
    print("0. Thoat tro choi")
    print("=" * 50)
    try:
        n = int(input("Nhap lua chon: "))
        if n not in [0, 1, 2, 3]:
            print("Loi: Vui long nhap so tu 1 den 3!")
            continue
        if n == 0:
            print("Cam on da su dung. Xin chao va hen gap lai!")
            print(f"- So tran thang: {thang} tran")
            print(f"- So tran hoa: {hoa} tran")
            print(f"- So tran thua: {thua} tran")
            break
        lua_chon = random.randint(1, 3)
        print(f"- Lua chon cua nguoi choi: {n}")
        print(f"- Lua chon cua may: {lua_chon}")

        if n == lua_chon:
            print("Hai ben hoa nhau! \n")
            hoa += 1
        elif (n == 1 and lua_chon == 3) or (n == 2 and lua_chon == 1) or (n == 3 and lua_chon == 2):
            print("Chuc mung! Ban da chien thang van nay. \n")
            thang += 1
        else:
            print("Ban da thua cuoc! \n")
            thua += 1
    except ValueError:
        print("Loi: Vui long nhap dung lua chon!")
