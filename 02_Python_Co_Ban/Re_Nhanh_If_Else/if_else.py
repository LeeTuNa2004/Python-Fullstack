# Xep loai nhan vien

ho_va_ten = input("Nhap ho va ten nhan vien: ")
diem_hieu_suat = float(input("Nhap diem (0.0 - 10.0): "))

if diem_hieu_suat >= 8.5:
    xep_loai = "Gioi"
    tien_thuong = float(5000000)
elif diem_hieu_suat >= 7.0:
    xep_loai = "Kha"
    tien_thuong = float(3000000)
elif diem_hieu_suat >= 5.0:
    xep_loai = "Trung binh"
    tien_thuong = float(1000000)
else: 
    xep_loai = "Can co gang"
    tien_thuong = float(0)

print(f"*" * 30)
print(f" He thong xep loai nhan vien")
print(f"*" * 30)
print(f"- Ho va ten: {ho_va_ten}")
print(f"- Diem hieu suat: {diem_hieu_suat}")
print(f"- Xep loai: {xep_loai}")
print(f"- Tien thuong: {tien_thuong:,.0f} VND")
print(f"*" * 30)
