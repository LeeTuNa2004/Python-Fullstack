# He thong phan tich va thong ke diem so

def phan_tich_diem(danh_sach_diem):
    if not danh_sach_diem: 
        return 0, 0, 0                  # Neu danh sach nhap vao la rong thi tra ve False de tranh loi chuong trinh
    
    dem = 0
    tong_diem = 0
    diem_max = danh_sach_diem[0]
    diem_min = danh_sach_diem[0]

    for i in danh_sach_diem:
        if i > diem_max:
            diem_max = i
        if i < diem_min:
            diem_min = i
        tong_diem += i
        dem += 1
    diem_trung_binh = tong_diem / dem
    return diem_max, diem_min, diem_trung_binh

def main():
    print("=== He thong phan tich diem so ===")
    print("Nhap 'q' bat cu luc nao de thoat chuong trinh.\n")
    while True:
        try:
            chuoi_nhap = input("Nhap danh sach diem (cach nhau bang dau phay): ").strip()
            if chuoi_nhap.lower() == 'q':                           # Ham chuyen chu thanh chu thuong
                print("Cam on da su dung he thong. Hen gap lai!")
                break

            cat_chuoi = chuoi_nhap.split(',')                       # Cat chuoi thanh cac chuoi con dua vao dau phay
            # Dung vong lap FOR de chuyen tung phan tu sang float va dua vao danh sach moi
            danh_sach_diem = []
            for phan_tu in cat_chuoi:
                danh_sach_diem.append(float(phan_tu.strip()))       # .strip() de xoa khoang trang thua neu co
                                                                    # .append() them mot phan tu moi vao cuoi DS
            diem_max, diem_min, diem_tb = phan_tich_diem(danh_sach_diem)

            print(f"- Diem cao nhat: {diem_max:,.2f} diem")
            print(f"- Diem thap nhat: {diem_min:,.2f} diem")
            print(f"- Diem trung binh: {diem_tb:,.2f} diem")
            print("-" * 40)
        except ValueError:
            print("Vui long nhap dung thong tin!\n")
            print("-" * 40)

if __name__ == "__main__":
    main()
