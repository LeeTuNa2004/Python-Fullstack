# He thong tinh tien sau giam gia

def tinh_tien_sau_giam_gia(don_gia, phan_tram_giam):
    tien_phai_tra = don_gia - don_gia * phan_tram_giam / 100
    if phan_tram_giam == 0:
        tien_phai_tra = don_gia
    return tien_phai_tra

while True:
    try:
        don_gia = float(input("Nhap don gia: "))
        phan_tram_giam = float(input("Nhap phan tram giam: "))
        # Chua kiem tra bien voi don gia am hoac % ngoai khoang pham vi

        hoa_don = tinh_tien_sau_giam_gia(don_gia, phan_tram_giam)
        print(f"So tien phai thanh toan: {hoa_don:,.2f} VND")
        break
    except ValueError:
        print("Vui long nhap dung thong tin!")
