# Toi uu theo Gemini

def danh_gia_nhan_su() -> None:
    print("-" * 30)
    print(" He thong danh gia nhan su")
    print("-" * 30)

    ho_va_ten = input("Nhap ho va ten nhan vien: ")
    diem_hieu_suat = float(input("Nhap diem (0.0 - 10.0): "))

    if ho_va_ten.isdigit() or len(ho_va_ten) < 3:                   # Them kiem tra dieu kien nhap lieu
        print("Loi: Ho va ten khong hop le")
        return
    else:
        print(f"Da ghi nhan ho va ten")

    if diem_hieu_suat >= 8.5:
        xep_loai = 'Gioi'
        tien_thuong = 5000000.0
    elif diem_hieu_suat >= 7.0:
        xep_loai = 'Kha'
        tien_thuong = 3000000.0
    elif diem_hieu_suat >= 5.0:
        xep_loai = 'Trung binh'
        tien_thuong = 1000000.0
    else:
        xep_loai = 'Can co gang'
        tien_thuong = 0.0

    print(f"- Ho va ten: {ho_va_ten}")
    print(f"- Diem hieu suat: {diem_hieu_suat}")
    print(f"- Xep loai: {xep_loai}")
    print(f"- Tien thuong: {tien_thuong:,.0f} VND")
    print("-" * 30)

if __name__ == "__main__":
    danh_gia_nhan_su()
