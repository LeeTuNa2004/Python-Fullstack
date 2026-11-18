# Tinh cuoc van chuyen giao hang thong minh

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

khach_hang_1 = tinh_tien_cuoc(10, 1, 0)
print(f"- Gia cuoc cua khach hang 1: {khach_hang_1:,.2f} VND")
khach_hang_2 = tinh_tien_cuoc(10, 5, 1)
print(f"- Gia cuoc cua khach hang 2: {khach_hang_2:,.2f} VND")