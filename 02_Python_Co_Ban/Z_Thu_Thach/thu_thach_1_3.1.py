# Huong dan toi uu tu Skill Gemini

def tinh_tien_sau_giam_gia(don_gia, phan_tram_giam):
    if don_gia < 0 or not(0 <= phan_tram_giam <= 100):          
        raise ValueError("Don gia phai duong va phan tram tu 0 den 100!")       # Kiểm tra biên dữ liệu đầu vào
    tien_phai_tra = don_gia * (1 - phan_tram_giam / 100)
    return tien_phai_tra

def main():
    print("=== He thong tinh tien sau giam gia ===")
    print("Nhap 'q' hoac '0' trong don gia neu muon thoat chuong trinh.\n")

    while True:
        try:
            nhap_don_gia = input("Nhap don gia: ")
            if nhap_don_gia.lower() == 'q' or nhap_don_gia == '0':
                print("Cam on da su dung he thong. Hen gap lai!")
                break
            don_gia = float(nhap_don_gia)
            phan_tram_giam = float(input("Nhap phan tram giam: "))

            hoa_don = tinh_tien_sau_giam_gia(don_gia, phan_tram_giam)
            print(f"So tien phai thanh toan: {hoa_don:,.2f} VND")
        except ValueError as e:
            print(f"Loi: {e}. Vui long nhap lai!\n")
            print("-" * 40)

if __name__ == "__main__":
    main()
