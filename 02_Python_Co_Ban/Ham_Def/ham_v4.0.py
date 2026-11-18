# He thong tinh tien dien sinh hoat - CLI

def tinh_tien_dien(so_kWh):
    if so_kWh <= 50:
        tien_chua_thue = so_kWh * 1806.0
        tong_thanh_toan = tien_chua_thue * 1.1
    elif 50 < so_kWh <= 100:
        tien_bac_1 = 50 * 1806.0
        so_kWh_moi = so_kWh - 50
        tien_bac_2 = so_kWh_moi * 1866
        tien_chua_thue = tien_bac_1 + tien_bac_2
        tong_thanh_toan = tien_chua_thue * 1.1
    else:
        tien_bac_1 = 50 * 1806.0
        tien_bac_2 = 50 * 1866.0
        so_kWh_moi = so_kWh - 100
        tien_bac_3 = so_kWh_moi * 2167
        tien_chua_thue = tien_bac_1 + tien_bac_2 + tien_bac_3
        tong_thanh_toan = tien_chua_thue * 1.1

    return tien_chua_thue, tong_thanh_toan

while True:
    try:
        print("He thong tinh tien dien sinh hoat")
        so_dien_cu = float(input("Nhap so dien cu: "))
        so_dien_moi = float(input("Nhap so dien moi: "))

        if so_dien_moi < so_dien_cu:
            print("Vui long nhap lai!")
            continue
        so_kWh = so_dien_moi - so_dien_cu
        tien_chua_thue, tong_thanh_toan = tinh_tien_dien(so_kWh)
        
        print("-" * 40)
        print(f"- Tong tien dien chua thue: {tien_chua_thue:,.2f} VND")
        print(f"- Tong tien thanh toan (da gom VAT): {tong_thanh_toan:,.2f} VND")
        print("-" * 40)
        break
    except ValueError:
        print("Loi: Vui long go dung yeu cau!")
