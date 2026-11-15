# Phan tich diem so lop hoc

danh_sach_diem = [8.5, 4.0, 6.5, 9.0, 3.5, 7.0, 5.5, 10.0, 4.5, 8.0]
tong_so_hoc_sinh = 0
so_luong_dat_yeu_cau = 0
so_luong_gioi_xuat_sac = 0

diem_max = danh_sach_diem[0]
diem_min = danh_sach_diem[0]
diem_tong = 0
dem = 0

for i in danh_sach_diem:
    diem_tong += i
    if i >= 8.0:
        so_luong_gioi_xuat_sac += 1
        if i > diem_max:                   # Loi phu thuoc vi tri khi tim MAX vi neu MAX < 8.0 thi se khong vao nhanh nay
            diem_max = i
    else:
        if i >= 5.0:                       # Loi lot luoi hoc sinh dat yeu cau vi chi loc theo khoang 5 <= diem <= 8
            so_luong_dat_yeu_cau += 1
        if i < diem_min:
            diem_min = i                   
    dem += 1

diem_trung_binh = diem_tong / dem

print(f"- Tong so luong hoc sinh trong lop: {dem} hoc sinh")
print(f"- So luong hoc sinh dat yeu cau (diem >= 5.0): {so_luong_dat_yeu_cau} hoc sinh")
print(f"- So luong hoc sinh gioi/xuat sac (diem >= 8.0): {so_luong_gioi_xuat_sac} hoc sinh")
print(f"- Diem so cao nhat: {diem_max}")
print(f"- Diem so thap nhat: {diem_min}")
print(f"- Diem trung binh toan lop: {diem_trung_binh}")
