# Tra cuu ma loi thiet bi mang (CLI)

ma_loi = {
    "404": "Khong tim thay tai nguyen",
    "500": "Loi he thong may chu",
    "403": "Khong co quyen truy cap"
}

ma_nhap = input("Nhap ma loi can tra loi: ").strip()

# Dung .get() de tra cuu an toan, neu khong co Key thi tra ve chuoi mac dinh thay vi loi KeyError
# Cu phap .get(key, gia_tri_mac_dinh): tim thay thi tra ve Value, khong thay thi tra ve chuoi mac dinh
mo_ta = ma_loi.get(ma_nhap, "Ma loi chua co trong danh sach.")
print(f"Ket qua [{ma_nhap}]: {mo_ta}")
