# He thong tra cuu gia va tinh tien cua hang

hang_hoa = {
    "tao": 20000,
    "cam": 35000,
    "chuoi": 15000,
    "xoai": 50000
}

# .lower() chuan hoa ve chu thuong de khop voi Key trong Dictionary
san_pham = input("Nhap ten mat hang muon mua: ").strip().lower()
try:
    so_luong = int(input("Nhap so luong muon mua: "))
except ValueError:
    print("Vui long chon so luong san pham!")    

if san_pham in hang_hoa:
    don_gia = hang_hoa[san_pham]
    hoa_don = don_gia * so_luong
    print("Hoa don thanh toan mat hang")
    print(f"- San pham: {san_pham}")
    print(f"- Don gia: {don_gia:,.2f} VND")
    print(f"- So luong: {so_luong}")
    print(f"- Tong tien: {hoa_don:,.2f} VND")
    print("-" * 40)
else:
    print(f"San pham '{san_pham}' hien khong co trong cua hang!")
