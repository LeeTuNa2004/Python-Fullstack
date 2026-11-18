# He thong quan ly gio hang va thanh toan thong minh

gia_san_pham = {
    "tao": 20000,
    "cam": 35000,
    "chuoi": 15000,
    "xoai": 50000,
    "sua": 12000
}

while True:
    try:
        mat_hang = input("Nhap mat hang muon mua: ").strip().lower()
        
        if mat_hang in gia_san_pham:
            so_luong = int(input("Nhap so luong muon mua: "))
            if so_luong <= 0:
                print(f"So luong phai luon duong!")
            else:
                don_gia = gia_san_pham[mat_hang]
                hoa_don = don_gia * so_luong
                print(f"So tien can thanh toan: {hoa_don:,.2f} VND")
        elif mat_hang == "thoat":
            print("\n=== Hoa don mua hang ===")
            print("Cam on da su dung. Hen gap lai!")
            break
        else:
            print(f"San pham '{mat_hang}' hien khong co trong cua hang!") 
    except ValueError:
        print(f"Vui long nhap dung thong tin!")
        continue
# Code dang tinh tien tuc thoi cho tung san pham, chua luu tru lai lich su cua nhung mon da mua nen khong tinh duoc hoa don
# Giai phap la tao gio hang luu tru san pham da mua bang .append(), khi "thoat" thi dung FOR de duyet qua no de tinh hoa don