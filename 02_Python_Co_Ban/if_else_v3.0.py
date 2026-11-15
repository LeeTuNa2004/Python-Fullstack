# He thong tinh tien ve xem phim thong minh

def tinh_tien_ve_xem_phim() -> None:
    khach_hang = input("Nhap ten khach hang: ")
    if not khach_hang.strip() or khach_hang.isdigit():
        print("Loi: Ten khach hang khong hop le!")
        return
    
    tuoi = int(input("Nhap tuoi khach hang: "))
    loai_ghe = int(input("Nhap loai ghe (1 - Ghe thuong, 2 - Ghe VIP, 3 - Ghe Double/Sweetbox): "))
    suat_chieu = int(input("Nhap suat chieu (1 - Suat thuong, 2 - Suat Chieu/Toi, 3 - Suat Cuoi tuan/Le): "))

    if tuoi < 0 or tuoi > 120 or loai_ghe not in [1, 2, 3] or suat_chieu not in [1, 2, 3]:
        print("Loi: Thong tin nhap vao khong hop le.")
        return

    if loai_ghe == 1:
        gia_ve = 60000.0
    elif loai_ghe == 2:
        gia_ve = 90000.0
    else:
        gia_ve = 140000.0

    if tuoi < 6:
        gia_ve *= 0.5
    elif tuoi >= 6 and tuoi < 18:
        gia_ve *= 0.8
    elif tuoi >= 60:
        gia_ve *= 0.7
    else:
        gia_ve += 0.0

    if suat_chieu == 2:
        gia_ve += 15000.0
    elif suat_chieu == 3:
        gia_ve += 30000.0
    else:
        gia_ve += 0.0

    print(f"-" * 30)
    print(f"Hoa don ve xem phim")
    print(f"-" * 30)

    print(f"- Khach hang: {khach_hang}")
    print(f"- Do tuoi: {tuoi} tuoi")
    print(f"- Loai ghe: {loai_ghe}")
    print(f"- Suat chieu: {suat_chieu}")
    print(f"- Tong tien: {gia_ve:,.0f} VND")
    print(f"-" * 30)

if __name__ == "__main__":
    tinh_tien_ve_xem_phim()
