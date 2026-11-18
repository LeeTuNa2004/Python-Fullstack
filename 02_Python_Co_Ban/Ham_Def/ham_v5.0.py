# He thong dat ve xem phim thong minh

def tinh_tien_ve(loai_ghe, la_cuoi_tuan, la_hssv):
    if loai_ghe == 1:
        loai_ghe = "Ghe thuong"
        gia_ve = 60000.0
    else:
        loai_ghe = "Ghe VIP"
        gia_ve = 100000.0
    if la_cuoi_tuan == 1:
        gia_ve *= 1.2
    if la_hssv == 1:
        gia_ve *= 0.85
    return loai_ghe, gia_ve

while True:
    try:
        loai_ghe = int(input("Nhap loai ghe (1: Ghe thuong / 2: Ghe VIP): "))
        if loai_ghe not in [1, 2]:
            print("Loi: Vui long nhap lai loai ghe!")
            continue
        la_cuoi_tuan = int(input("Nhap lua chon (1: Cuoi tuan / 0: Ngay thuong): "))
        la_hssv = int(input("Trang thai khach hang (1: HSSV / 0: Thuong): "))

        loai_ghe_1, gia_ve_1 = tinh_tien_ve(loai_ghe, la_cuoi_tuan, la_hssv)
        print("-" * 50)
        print(f"- Loai ghe da chon: {loai_ghe_1}")
        print(f"- Tien ve phai tra: {gia_ve_1:,.2f} VND")
        print("-" * 50)
        break
    except ValueError:
        print("Vui long nhap dung thong tin!")
