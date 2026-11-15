# May ATM Mini - Xu ly giao dich rut tien

so_du = 2000000.0
danh_sach_yeu_cau_rut = [300000, 2500000, 500000, 400000, 1000000]

tong_so_tien_da_rut = 0
dem = 0

for i in danh_sach_yeu_cau_rut:
    if i > so_du:
        print(f"Giao dich that bai: So du khong du!")
        continue

    so_du = so_du - i
    tong_so_tien_da_rut += i
    dem += 1

    print(f"- So tien rut thanh cong: {i:,.0f} VND")
    print(f"- So du con lai cua tai khoan: {so_du:,.0f} VND")

    if so_du == 0:
        print(f"Tai khoan da het tien. Ket thuc phien giao dich som!")
        break

print(f"- Tong so tien da rut thanh cong: {tong_so_tien_da_rut:,.0f} VND")
print(f"- So du thuc te con lai trong tai khoan: {so_du:,.0f} VND")
print(f"- Tong so lan rut tien thanh cong: {dem} lan")
