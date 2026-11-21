# Tu dien Anh - Viet tuong tac lien tuc (CLI)

# Buoc 1: Xay dung khung Menu va tu dien goc
tu_dien_anh_viet = {
    "hello": "xin chao",
    "python": "ngon ngu lap trinh",
    "code": "ma nguon",
    "mentor": "nguoi huong dan"
}

while True:
    print("\n===== TU DIEN ANH - VIET =====")
    print("1. Tra cuu tu vung")
    print("2. Them tu vung moi")
    print("3. Xoa tu vung moi")
    print("4. Xem toan bo tu vung")
    print("5. Thoat chuong trinh")
    print("=" * 50)

    lua_chon = input("Nhap lua chon (1-5): ").strip()

    # Buoc 2: Thuc hien chuc nang 1
    if lua_chon == "1":
        tu_vung = input("Nhap tu can tra cuu: ").strip().lower()
        if tu_vung in tu_dien_anh_viet:   
            # Lấy trực tiếp nghĩa theo Key, không lặp toàn bộ dictionary 
            nghia = tu_dien_anh_viet[tu_vung]                   
            print(f"Nghia cua tu la: '{nghia}'")
        else:
            print(f"Khong tim thay '{tu_vung}' trong tu dien!")

    # Buoc 3: Thuc hien chuc nang 2
    elif lua_chon == "2":
        them_tu_moi = input("Nhap tu moi can them: ").strip().lower()
        if not them_tu_moi:
            print("Tu vung khong duoc de trong!")
        elif them_tu_moi in tu_dien_anh_viet:
            print(f"Tu '{them_tu_moi}' da co trong tu dien. Vui long them tu khac!")
        else:
            nghia_tuong_ung = input("Nhap nghia cua tu moi: ").strip().lower()
            if not nghia_tuong_ung:
                print("Nghia cua tu khong duoc de trong!")
            else:
                # Gán theo key mới để thêm vào dictionary hiện có (không ghi đè cả dictionary)
                tu_dien_anh_viet[them_tu_moi] = nghia_tuong_ung
                print(f"Da them '{them_tu_moi}' vao tu dien Anh - Viet!")

    # Buoc 4: Thuc hien chuc nang 3
    elif lua_chon == "3":
        xoa_tu = input("Nhap tu muon xoa: ").strip().lower()
        if not xoa_tu:
            print("Tu can xoa khong duoc de trong!")
        elif xoa_tu in tu_dien_anh_viet:
            # Xóa cặp key-value theo key đã chuẩn hóa
            del tu_dien_anh_viet[xoa_tu]
            print(f"Da xoa '{xoa_tu}' khoi tu dien!")
        else:
            print(f"Tu '{xoa_tu}' khong co trong tu dien!")

    # Buoc 5: Thuc hien chuc nang 4
    elif lua_chon == "4":
        if not tu_dien_anh_viet:
            print("Tu dien dang trong, khong co gi de hien thi.")
        else:
            stt = 1
            for tu, nghia in tu_dien_anh_viet.items():
                print(f"- {stt}: {tu} - {nghia}")
                stt += 1
            print("=" * 50)

    # Thoat chuong trinh
    elif lua_chon == "5":
        print("Cam on da su dung. Xin hen gap lai!")
        break
    else:
        print("Loi: Lua chon khong hop le. Vui long nhap lai!")
