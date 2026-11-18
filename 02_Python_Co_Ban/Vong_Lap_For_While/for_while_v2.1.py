# Huong dan tu Skill Gemini

danh_sach_diem = [8.5, 4.0, 6.5, 9.0, 3.5, 7.0, 5.5, 10.0, 4.5, 8.0]

tong_so_hoc_sinh = len(danh_sach_diem)
so_luong_dat_yeu_cau = 0
so_luong_gioi_xuat_sac = 0
diem_tong = 0

diem_max = danh_sach_diem[0]
diem_min = danh_sach_diem[0]

for i in danh_sach_diem:
    diem_tong += i
    if i >= 5.0:
        so_luong_dat_yeu_cau += 1
    if i >= 8.0:
        so_luong_gioi_xuat_sac += 1
    if i > diem_max:
        diem_max = i
    if i < diem_min:
        diem_min = i

diem_trung_binh = diem_tong / tong_so_hoc_sinh

print(f"- Tong so luong hoc sinh trong lop: {tong_so_hoc_sinh} hoc sinh")
print(f"- So luong hoc sinh dat yeu cau (diem >= 5.0): {so_luong_dat_yeu_cau} hoc sinh")
print(f"- So luong hoc sinh gioi/xuat sac (diem >= 8.0): {so_luong_gioi_xuat_sac} hoc sinh")
print(f"- Diem so cao nhat: {diem_max}")
print(f"- Diem so thap nhat: {diem_min}")
print(f"- Diem trung binh toan lop: {diem_trung_binh:.2f}")
