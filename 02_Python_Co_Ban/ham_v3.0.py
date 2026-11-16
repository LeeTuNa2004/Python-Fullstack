# He thong thanh toan gio hang thong minh

def thanh_toan(tong_tien_hang, la_thanh_vien_vip, co_voucher):
    tien_giam_gia = 0
    sau_giam_gia = 0
    if la_thanh_vien_vip == 1:
        tien_giam_gia = tong_tien_hang * 0.1
        sau_giam_gia = tong_tien_hang * 0.9
    else:
        sau_giam_gia = tong_tien_hang
    
    if co_voucher == 1:
        tien_giam_gia = tien_giam_gia + 50000.0
        sau_giam_gia -= 50000.0
        
    sau_giam_gia = sau_giam_gia + sau_giam_gia * 0.08
    return tien_giam_gia, sau_giam_gia

tien_giam_gia_1, tong_thanh_toan_1 = thanh_toan(1000000.0, 1, 1)
tien_giam_gia_2, tong_thanh_toan_2 = thanh_toan(1000000.0, 1, 0)
tien_giam_gia_3, tong_thanh_toan_3 = thanh_toan(1000000.0, 0, 1)
tien_giam_gia_4, tong_thanh_toan_4 = thanh_toan(1000000.0, 0, 0)
print(f"- Tong so tien duoc giam gia: {tien_giam_gia_1:,.2f} VND")
print(f"- So tien thuc te khach phai tra: {tong_thanh_toan_1:,.2f} VND")
print(f"- Tong so tien duoc giam gia: {tien_giam_gia_2:,.2f} VND")
print(f"- So tien thuc te khach phai tra: {tong_thanh_toan_2:,.2f} VND")
print(f"- Tong so tien duoc giam gia: {tien_giam_gia_3:,.2f} VND")
print(f"- So tien thuc te khach phai tra: {tong_thanh_toan_3:,.2f} VND")
print(f"- Tong so tien duoc giam gia: {tien_giam_gia_4:,.2f} VND")
print(f"- So tien thuc te khach phai tra: {tong_thanh_toan_4:,.2f} VND")
