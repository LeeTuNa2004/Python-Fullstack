# Trinh phan tich giao dich tai chinh tren Terminal

danh_sach_giao_dich = [500, -200, 1200, -50, -300, 2500, -1000, 150]
tong_so_du = 0
tong_tien_nap = 0
tong_tien_rut = 0
dem = 0
nap_lon_nhat = 0
rut_sau_nhat = 0                # Loi logic neu chi nap thi giao dich luon duong nen khong thoa man dieu kien
trang_thai = True               # Dang bi gan cung gia tri True thay vi danh gia dua tren tong so du tai khoan
dem_tuyet_doi = 0

for i in danh_sach_giao_dich:
    tong_so_du += i

    if i > 0:
        tong_tien_nap += i
    else:
        tong_tien_rut += i

    if i < -200:
        dem += 1
    if i > nap_lon_nhat:
        nap_lon_nhat = i
    if i < rut_sau_nhat:
        rut_sau_nhat = i
    if abs(i) > 500:
        dem_tuyet_doi += 1
    elif i < -1000:             # Dat sai cau truc re nhanh if-elif-else
        print(f"Canh bao giao dich bat thuong!")

print(f"-" * 30)
print(f"He thong phan tich giao dich tai chinh")
print(f"-" * 30)

print(f"- Tong so du cuoi cung: {tong_so_du:,.0f} VND")
print(f"- Tong tien nap vao: {tong_tien_nap:,.0f} VND")
print(f"- Tong tien da rut ra: {tong_tien_rut:,.0f} VND")
print(f"- So luong giao dich rut tien lon (< -200): {dem} giao dich")
print(f"- Khoan giao dich ky luc: ")
print(f"   - Nap lon nhat: {nap_lon_nhat:,.0f} VND")
print(f"   - Rut sau nhat: {rut_sau_nhat:,.0f} VND")
print(f"- Danh gia trang thai tai khoan: {trang_thai}")
print(f"- Canh bao dong tien > 500: {dem_tuyet_doi} giao dich") 
