# He thong quan ly gio hang va thanh toan thong minh

gia_san_pham = {
    "tao": 20000,
    "cam": 35000,
    "chuoi": 15000,
    "xoai": 50000,
    "sua": 12000
}

gio_hang = []                         # Khoi tao mot danh sach (list) lam "gio hang" de luu tru cac mon hang da mua

print("=== Sieu thi MINI ===")
print("Cac mat hang co san: tao, cam, chuoi, xoai, sua")
print("Go 'thoat' bat cu luc nao de ket thuc mua sam va in hoa don.\n")

while True:
    mat_hang = input("Nhap mat hang muon mua: ").strip().lower()

    if mat_hang == "thoat":
        break
    if mat_hang in gia_san_pham:
        try:
            so_luong = int(input("Nhap so luong muon mua: "))
            if so_luong <= 0:
                print("So luong mua luon duong!")
            else:
                don_gia = gia_san_pham[mat_hang]
                thanh_tien = don_gia * so_luong
                san_pham_mua = {                        # Khoi tao Dictionary de luu tru thong tin san pham
                    "ten": mat_hang,
                    "don_gia": don_gia,
                    "so_luong": so_luong,
                    "thanh_tien": thanh_tien
                }
                gio_hang.append(san_pham_mua)           # .append() them mot phan tu moi vao cuoi danh sach
                print(f"Da them {so_luong} {mat_hang} vao gio hang. Tam tinh: {thanh_tien:,.2f} VND\n")
        except ValueError:
            print("Loi: Vui long nhap dung so luong!")
    else:
        print(f"San pham '{mat_hang}' hien khong co trong cua hang!\n")

print("\n" + "=" * 50)
print("=== Hoa don thanh toan chi tiet ===")

if not gio_hang:
    print("Gio hang dang trong! Khong co gi de thanh toan.")
else:
    tong_tien_phai_tra = 0
    for item in gio_hang:                               # Duyet lan luot tung san pham co trong gio hang
        print(f"- {item['ten'].capitalize()} | Don gia: {item['don_gia']:,.0f} VND | SL: {item['so_luong']} | Thanh tien: {item['thanh_tien']:,.0f} VND")
        tong_tien_phai_tra += item['thanh_tien']

    print("=" * 50)
    print(f"Tong tien phai thanh toan: {tong_tien_phai_tra:,.2f} VND")

print("=" * 50)
print("Cam on da mua sam. Xin chao va hen gap lai!")
