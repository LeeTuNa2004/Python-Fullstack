# He thong xep loai hoc luc thong minh - Skill Gemini

def xep_loai_hoc_luc(diem_toan, diem_van, diem_anh):
    diem_trung_binh = ((diem_toan * 2) + (diem_van * 2) + diem_anh) / 5
    if diem_trung_binh >= 8.5:
        xep_loai = "Gioi"
    elif 6.5 <= diem_trung_binh < 8.5:
        xep_loai = "Kha"
    elif 5.0 <= diem_trung_binh < 6.5:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Yeu"

    return diem_trung_binh, xep_loai            # Tra ve dong thoi 2 gia tri, Python tu dong dong goi thanh Tuple

try:
    print("=== He thong xep loai hoc luc ===")
    toan = float(input("Nhap diem mon Toan: "))
    van = float(input("Nhap diem mon Van: "))
    anh = float(input("Nhap diem mon Anh: "))

    diem_tb, danh_hieu = xep_loai_hoc_luc(toan, van, anh)           # Giai nen truc tiep khi tra ve nhieu gia tri
    print(f"-" * 35)
    print(f"- Diem trung binh: {diem_tb:,.2f} diem")
    print(f"- Xep loai hoc luc: {danh_hieu}")
    print(f"-" * 35)
except ValueError:
    print("Loi: Vui long chi nhap so hop le!")