# Tinh cuoc van chuyen giao hang thong minh tren Terminal - CLI
# Ham tra ve gia tri

def tinh_tien_cuoc(khoang_cach, trong_luong, la_khach_vip):
    if khoang_cach <= 5:
        cuoc_phi = 15000.0
    else:
        cuoc_phi = 15000.0 + 3000.0 * (khoang_cach - 5)

    if trong_luong > 2:
        so_kg_vuot = trong_luong - 2
        cuoc_phi += 10000.0 * so_kg_vuot

    if la_khach_vip:
        cuoc_phi *= 0.85

    return cuoc_phi

try:
    kc = float(input("Nhap khoang cach giao hang (km): "))
    tl = float(input("Nhap trong luong goi hang (kg): "))
    vip = int(input("Trang thai cua khach hang: "))

    if vip == 1:
        is_vip = True
    else:
        is_vip = False

    tong_tien = tinh_tien_cuoc(kc, tl, is_vip)
    print(f"- Tong tien cuoc phi phai tra: {tong_tien:,.2f} VND")
except ValueError:
    print("Loi: Vui long chi nhap so hop le!")
