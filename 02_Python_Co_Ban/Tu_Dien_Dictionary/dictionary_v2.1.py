# He thong tra cuu gia va tinh tien cua hang

hang_hoa = {
    "tao": 20000,
    "cam": 35000,
    "chuoi": 15000,
    "xoai": 50000
}

san_pham = input("Nhap ten mat hang muon mua: ").strip().lower()

if san_pham in hang_hoa:                                            # Kiem tra ton tai trong Dictionary truoc
    don_gia = hang_hoa[san_pham]

    try:
        so_luong = int(input("Nhap so luong muon mua: "))
        if so_luong <= 0:                                           # Kiem tra so luong hop le
            print("So luong mua luon duong!")
        else:
            hoa_don = don_gia * so_luong
            print("\n--- Hoa don thanh toan ---")
            print(f"- San pham: {san_pham}")
            print(f"- Don gia: {don_gia:,.2f} VND")
            print(f"- So luong: {so_luong}")
            print(f"- Tong tien: {hoa_don:,.2f} VND")
            print("-" * 40)
    except ValueError:
        print("Loi: Vui long nhap so luong hop le!")
else:
    print(f"San pham '{san_pham}' hien khong co trong cua hang!")
