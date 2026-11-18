# He thong xep loai hoc luc thong minh
# Ham tra ve nhieu gia tri (return multiple values)

def xep_loai_hoc_luc(diem_toan, diem_van, diem_anh):
    diem_trung_binh = ((diem_toan * 2) + (diem_van * 2) + diem_anh) / 5
    xep_loai = str(" ")

    if diem_trung_binh >= 8.5:
        xep_loai = "Gioi"
    elif 6.5 <= diem_trung_binh < 8.5:
        xep_loai = "Kha"
    elif 5.0 <= diem_trung_binh < 6.5:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Yeu"
    
    return diem_trung_binh, xep_loai

try: 
    toan = float(input("Nhap diem mon Toan: "))
    van = float(input("Nhap diem mon Van: "))
    anh = float(input("Nhap diem mon Anh: "))

    diem_tb = xep_loai_hoc_luc(toan, van, anh)[0]           # Su dung cach truy xuat phan tu 0 trong ham
    print(f"- Ket qua hoc tap: {diem_tb:,.2f}")
    xep_loai = xep_loai_hoc_luc(toan, van, anh)[1]          # Su dung cach truy xuat phan tu 1 trong ham
    print(f"- Xep loai hoc luc: {xep_loai}")
except ValueError:
    print("Loi: Vui long nhap dung ki tu!")