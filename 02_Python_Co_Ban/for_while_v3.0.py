# Quan ly gio hang thuong mai dien tu

danh_sach_gia = [150000, 45000, 1200000, 320000, 85000, 2500000, 60000]

tong_gia_tri = 0
dem = 0

dat_nhat = danh_sach_gia[0]
re_nhat = danh_sach_gia[0]

for i in danh_sach_gia:
    tong_gia_tri += i
    if i > 500000.0:
        dem += 1

    if i > dat_nhat:
        dat_nhat = i
    if i < re_nhat:
        re_nhat = i

if tong_gia_tri > 3000000:
    gia_moi = tong_gia_tri - tong_gia_tri * 0.15
else:
    gia_moi = tong_gia_tri

print(f"- Tong gia tri gio hang truoc khi giam gia: {tong_gia_tri:,.0f} VND")
print(f"- So luong san pham gia tri cao hon 500,000 VND: {dem}")
print(f"- Mon do dat nhat: {dat_nhat:,.0f} VND")
print(f"- Mon do re nhat: {re_nhat:,.0f} VND")
print(f"- So tien can phai thanh toan cua gio hang: {gia_moi:,.0f} VND")
