# Tu dien Anh - Viet (CLI)
# Da toi uu bang cach tach tung chuc nang ra ham (def)

tu_dien_anh_viet = {
    "hello": "xin chao",
    "python": "ngon ngu lap trinh",
    "code": "ma nguon",
    "mentor": "nguoi huong dan"
}

def tra_cuu_tu(tu_dien) -> None:
    tu_vung = input("Nhap tu can tra cuu: ").strip().lower()
    if not tu_vung:
        print("Tu can tra cuu khong duoc de trong!")
        return
    if tu_vung in tu_dien:
        nghia = tu_dien[tu_vung]
        print(f"Nghia cua '{tu_vung}' la: '{nghia}'")
    else:
        print(f"Khong tim thay '{tu_vung}' trong tu dien!")

def them_tu(tu_dien) -> None:
    them_tu_moi = input("Nhap tu moi can them: ").strip().lower()
    if not them_tu_moi:
        print("Tu moi khong duoc de trong!")
        return
    if them_tu_moi in tu_dien:
        print(f"Tu '{them_tu_moi}' da co trong tu dien. Vui long them tu khac!")
        return
    nghia_tuong_ung = input("Nhap nghia cua tu moi: ").strip().lower()
    if not nghia_tuong_ung:
        print("Nghia cua tu khong duoc de trong!")
        return
    tu_dien[them_tu_moi] = nghia_tuong_ung
    print(f"Da them '{them_tu_moi}' vao tu dien Anh - Viet!")

def xoa_tu(tu_dien) -> None:
    tu_can_xoa = input("Nhap tu can xoa: ").strip().lower()
    if not tu_can_xoa:
        print("Tu can xoa khong duoc de trong!")
        return
    if tu_can_xoa in tu_dien:
        del tu_dien[tu_can_xoa]
        print(f"Da xoa '{tu_can_xoa}' khoi tu dien!")
    else:
        print(f"Tu '{tu_can_xoa}' khong co trong tu dien!")

def hien_thi_tu_dien(tu_dien) -> None:
    if not tu_dien:
        print("Tu dien dang trong, khong co gi de hien thi!")
        return
    print("\n--- Danh sach tu vung ---")
    # enumerate(..., start=1) tu dong danh so thu tu tu 1 ma khong can bien dem thu cong
    for stt, (tu, nghia) in enumerate(tu_dien.items(), start=1):
        print(f"- {stt}: {tu} - {nghia}")
    print("=" * 50)

while True:
    print("\n=== TU DIEN ANH - VIET ===")
    print("1. Tra cuu tu vung")
    print("2. Them tu vung moi")
    print("3. Xoa tu vung")
    print("4. Xem toan bo tu vung")
    print("5. Thoat chuong trinh")
    print("=" * 50)

    lua_chon = input("Nhap lua chon: ").strip()
    if lua_chon == "1":
        tra_cuu_tu(tu_dien_anh_viet)
    elif lua_chon == "2":
        them_tu(tu_dien_anh_viet)
    elif lua_chon == "3":
        xoa_tu(tu_dien_anh_viet)
    elif lua_chon == "4":
        hien_thi_tu_dien(tu_dien_anh_viet)
    elif lua_chon == "5":
        print("Cam on da su dung. Xin hen gap lai!")
        break
    else:
        print("Loi: Lua chon khong hop le. Vui long nhap lai!")
