# Tra cuu mon, nhap so luong & Tinh tong tien

menu = {
    "ca_phe": 25000,
    "tra_dao": 30000,
    "matcha": 35000
}

# Tinh tong tien cho 1 mon, tra ve None neu khong tim thay hoac so luong <= 0
def tinh_tien_mon(menu_dict, ten_mon, so_luong):
    don_gia = menu_dict.get(ten_mon)
    if don_gia is None or so_luong <= 0:
        return None
    return don_gia * so_luong

def main():
    mon_nhap = input("Nhap ten mon: ").strip().lower()
    so_luong_nhap = input("Nhap so luong: ").strip()
    try:
        so_luong = int(so_luong_nhap)
    except ValueError:
        print("So luong phai lon hon 0.")
        return
    if mon_nhap not in menu:
        print("Mon chua co trong Menu.")
        return
    tong_tien = tinh_tien_mon(menu, mon_nhap, so_luong)
    # Neu so luong am thi tong tien phai tra ve None
    if tong_tien is None:
        print("So luong khong hop le.")
        return
    print(f"Mon: {mon_nhap} | SL: {so_luong} | Tong tien: {tong_tien} VND")

if __name__ == "__main__":
    main()
