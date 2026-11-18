# He thong bao cao va loc diem so hoc sinh

danh_sach_lop = {
    "An": 8.5,
    "Binh": 7.0,
    "Chi": 9.2,
    "Dung": 6.5,
    "Emi": 4.5,
    "Phuc": 8.0
}

diem_tong = 0
diem_tb = 0
dem = 0

try:
    diem_chuan = float(input("Nhap diem chuan can dat: "))
    # .items() boc tach dong thoi ca Key lan Value ra khoi tu dien trong 1 vong lap FOR
    for ten, diem in danh_sach_lop.items():
        diem_tong += diem
        dem += 1
    
    diem_tb = diem_tong / dem
    print("\n=== Bao cao ket qua hoc tap ===")
    print(f"- Diem trung binh ca lop: {diem_tb:,.2f} diem")
    print(f"- Danh sach cac hoc sinh dat tu {diem_chuan} diem tro len: ")

    for ten, diem in danh_sach_lop.items():
        if diem >= diem_chuan:
            print(f"   + {ten}: {diem:,.2f} diem")
            co_hoc_sinh_dat = True

    if not co_hoc_sinh_dat:
        print(f"Khong co hoc sinh nao dat tu {diem_chuan} diem tro len!")
    print("-" * 50)
except ValueError:
    print("Vui long nhap dung thong tin!")
