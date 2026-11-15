# He thong tinh cuoc phi giao hang thong minh

def tinh_cuoc_phi_giao_hang() -> None:
    khach_hang = input("Nhap ten khach hang: ")
    khoang_cach = float(input("Nhap khoang cach (km): "))
    loai_dich_vu = int(input("Nhap loai dich vu (1 - Giao thuong, 2 - Giao hoa toc): "))

    if khoang_cach < 0 or loai_dich_vu not in [1, 2]:
        print("Loi: Khoang cach hoac loai dich vu khong hop le")
        return
    else:
        print(f"Da ghi nhan thong tin khach hang: {khach_hang}")
        
    if khoang_cach >= 10:
        cuoc_phi = 40000.0
    elif khoang_cach >= 3 and khoang_cach <= 10:
        cuoc_phi = 25000.0
    else:
        cuoc_phi = 15000.0

    if loai_dich_vu == 2:
        cuoc_phi += 20000.0
    else:
        cuoc_phi += 0.0

    print(f"*" * 30)
    print(f" He thong tinh cuoc phi giao hang")
    print(f"*" * 30)
    print(f"- Khach hang: {khach_hang}")
    print(f"- Khoang cach: {khoang_cach} km")
    print(f"- Loai dich vu: {'Giao hoa toc' if loai_dich_vu == 2 else 'Giao thuong'}")
    print(f"Cuoc phi giao hang: {cuoc_phi} VND")
    print(f"*" * 30)

if __name__ == "__main__":
    tinh_cuoc_phi_giao_hang()
