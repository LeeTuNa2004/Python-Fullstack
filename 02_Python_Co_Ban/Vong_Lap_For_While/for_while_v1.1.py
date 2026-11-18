# Huong dan tu Skill Gemini

danh_sach_giao_dich = [500, -200, 1200, -50, -300, 2500, -1000, 150]

tong_so_du = 0
tong_tien_nap = 0
tong_tien_rut = 0
dem_giao_dich_rut_lon = 0
dem_giao_dich_tuyet_doi = 0

# Meo: Khoi tao MIN/MAX bang phan tu dau tien cua danh sach
# de tranh loi logic khi toan bo du lieu la so duong hoac am
nap_lon_nhat = danh_sach_giao_dich[0]
rut_sau_nhat = danh_sach_giao_dich[0]

for i in danh_sach_giao_dich:
    tong_so_du += i

    if i > 0:
        tong_tien_nap += i
        if i > nap_lon_nhat:
            nap_lon_nhat = i
    else:
        tong_tien_rut += i
        if i < rut_sau_nhat:
            rut_sau_nhat = i

    if i < -200:
        dem_giao_dich_rut_lon += 1
    if abs(i) > 500:
        dem_giao_dich_tuyet_doi += 1
    if i < -1000:
        print(f"Phat hien giao dich rut tien sau bat thuong ({i:,.0f} VND)!")

if tong_so_du < 0:
    trang_thai = "Tai khoan khong the giao dich."
else:
    trang_thai = "Tai khoan hoat dong an toan."

print(f"-" * 45)
print(f"He thong phan tich tai chinh")
print(f"-" * 45)

print(f"- Tong so du: {tong_so_du:,.0f} VND")
print(f"- Tong tien nap vao: {tong_tien_nap:,.0f} VND")
print(f"- Tong tien da rut ra: {tong_tien_rut:,.0f} VND")
print(f"- So luong giao dich rut tien lon (< -200): {dem_giao_dich_rut_lon} giao dich")
print(f"- Khoan giao dich ky luc:")
print(f"   - Nap lon nhat: {nap_lon_nhat:,.0f} VND")
print(f"   - Rut lon nhat: {rut_sau_nhat:,.0f} VND")
print(f"- Danh gia trang thai tai khoan: \n -> {trang_thai}")
print(f"- Canh bao dong tien > 500: {dem_giao_dich_tuyet_doi} giao dich")
print(f"-" * 50) 
