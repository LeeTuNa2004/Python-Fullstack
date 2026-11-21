# Tra cuu & Quy doi trang thai cong thiet bi (CLI)

trang_thai = {
    "up": "Hoat dong binh thuong",
    "down": "Mat ket noi",
    "admin-down": "Dang bi khoa"
}

def mo_ta_trang_thai(bang_trang_thai, ma_trang_thai):
    return bang_trang_thai.get(ma_trang_thai, "Trang thai khong xac dinh.")

def main():
    ma_nhap = input("Nhap ma trang thai: ").strip().lower()
    mo_ta = mo_ta_trang_thai(trang_thai, ma_nhap)
    print(f"Trang thai ({ma_nhap}): {mo_ta}")

if __name__ == "__main__":
    main()
